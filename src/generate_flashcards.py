from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import TYPE_CHECKING, Any, TypeAlias

import pandas as pd
from dotenv import load_dotenv
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_core.runnables.base import RunnableSerializable
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

# for typing purposes only
if TYPE_CHECKING:
    from pandas import DataFrame

ChainType: TypeAlias = RunnableSerializable[dict[Any, Any], Any]

# defining logging config
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

# loading api key and defining vars
load_dotenv()


# checking if .env vars are set
def get_deck_name() -> str:
    deck_name: str = os.environ.get("DECK_NAME", "default_deck_name")
    return deck_name


def get_api_key() -> str:
    OPENAI_API_KEY: str | None = os.environ.get("OPENAI_API_KEY")
    if OPENAI_API_KEY is None:
        raise ValueError("No API key set")
    return OPENAI_API_KEY


# defining path to dirs
deck_name = get_deck_name()
data_dir: Path = Path("data")
csv_file_path: Path = data_dir / f"{deck_name}.csv"

# llm params
OPENAI_API_KEY = get_api_key()
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
    Generates flashcards from the given input text,
    formats them based on the user's prompt,
    and saves the output to a CSV file in the data directory
    """

    llm: ChatOpenAI = ChatOpenAI(model=MODEL, temperature=TEMPERATURE)

    logging.info("Creating model...")

    parser: PydanticOutputParser[FlashCardArray] = PydanticOutputParser(
        pydantic_object=FlashCardArray
    )

    logging.info("Creating parser...")

    llm_prompt: PromptTemplate = PromptTemplate(
        template=prompt,
        input_variables=["input_text"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    logging.info("Creating prompt...")

    chain: ChainType = llm_prompt | llm | parser

    logging.info("Parsing and validating input data...")

    output = chain.invoke({"input_text": input})
    list_of_flashcards: list[str] = [card.dict() for card in output.flashcards]
    return pd.DataFrame(list_of_flashcards)


def write_flashcards_to_csv(dataframe: DataFrame, csv_file_path: Path) -> None:
    logging.info("Writing to file...")
    if csv_file_path.is_file():
        dataframe.to_csv(csv_file_path, mode="a", header=False, index=False)
    else:
        dataframe.to_csv(csv_file_path, mode="w", header=False, index=False)


def main() -> None:
    try:
        with open("src/input.txt") as f:
            input_text = f.read()

        with open("src/prompt.txt") as f:
            user_prompt = f.read()

        df = llm_generate_flashcards(input_text, user_prompt)
        write_flashcards_to_csv(df, csv_file_path)
        logging.info("Done \U0001f600")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return


if __name__ == "__main__":
    main()
