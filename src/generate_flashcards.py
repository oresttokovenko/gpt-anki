from __future__ import annotations
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from pathlib import Path
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from typing import TYPE_CHECKING
import pandas as pd
import logging
import os

if TYPE_CHECKING:
    # for typing purposely only
    from pandas import DataFrame
    from langchain.chains.sequential import SequentialChain

# defining logging config
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

# loading api key and defining vars
load_dotenv()
deck_name: str | None = os.environ.get("DECK_NAME")
if deck_name is None:
    deck_name = "default_deck_name"

data_dir: str = Path("data")
csv_file_path: str = data_dir / f"{deck_name}.csv"

# llm params
OPENAI_API_KEY: str = os.environ.get("OPENAI_API_KEY")
MODEL: str = "gpt-4"
TEMPERATURE: float = 0.0


# datatype validation
class FlashCard(BaseModel):
    question: str = Field(description="The question for the flashcard")
    answer: str = Field(description="The answer for the flashcard")


class FlashCardArray(BaseModel):
    flashcards: list[FlashCard]


def llm_generate_flashcards(input: str, prompt: str) -> DataFrame:
    """
    Generates flashcards from the given input text, formats them based on the user's prompt,
    and saves the output to a CSV file in the data directory
    """

    llm: ChatOpenAI = ChatOpenAI(model=MODEL, temperature=TEMPERATURE)

    logging.info("Creating model...")

    parser: PydanticOutputParser = PydanticOutputParser(pydantic_object=FlashCardArray)

    logging.info("Creating parser...")

    llm_prompt: PromptTemplate = PromptTemplate(
        template=prompt,
        input_variables=["input_text"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    logging.info("Creating prompt...")

    chain: SequentialChain = llm_prompt | llm | parser

    logging.info("Parsing and validating input data...")

    output: dict = chain.invoke({"input_text": input})
    list_of_flashcards = [card.dict() for card in output.flashcards]
    return pd.DataFrame(list_of_flashcards)


def write_flashcards_to_csv(dataframe: DataFrame, csv_file_path: str) -> None:
    logging.info("Writing to file...")
    if os.path.isfile(csv_file_path):
        dataframe.to_csv(csv_file_path, mode="a", header=False, index=False)
    else:
        dataframe.to_csv(csv_file_path, mode="w", header=False, index=False)


def main() -> None:
    try:
        with open("src/input.txt", "r") as f:
            input_text = f.read()

        with open("src/prompt.txt", "r") as f:
            user_prompt = f.read()

        df = llm_generate_flashcards(input_text, user_prompt)
        write_flashcards_to_csv(df, csv_file_path)
        logging.info("Done \U0001f600")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return


if __name__ == "__main__":
    main()
