import csv
import logging
import os
import random
from pathlib import Path

from dotenv import load_dotenv
from genanki import Deck, Model, Note, Package

load_dotenv()

# defining logging config
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")


def get_deck_name() -> str:
    deck_name: str = os.environ.get("DECK_NAME", "default_deck_name")
    return deck_name


output_deck_name = get_deck_name()

# defining path to dirs
data_dir: Path = Path("data")
csv_file_path: Path = data_dir / f"{output_deck_name}.csv"

deck_dir: Path = Path("decks")
output_file_path: Path = deck_dir / f"{output_deck_name}.apkg"


def read_csv(file_path: Path) -> list[tuple[str, str]]:
    with Path.open(file_path, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        qa_list = [(row[0], row[1]) for row in csv_reader]
    return qa_list


def create_anki_deck(deck_name: str, qa_list: list[tuple[str, str]]) -> Deck:
    model_id = random.randrange(1 << 30, 1 << 31)
    my_model = Model(
        model_id,
        "Simple Model",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
        ],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Question}}",
                "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ],
    )

    deck_id = random.randrange(1 << 30, 1 << 31)
    my_deck = Deck(deck_id, deck_name)

    for question, answer in qa_list:
        my_note = Note(model=my_model, fields=[question, answer])
        my_deck.add_note(my_note)

    return my_deck


def export_anki_deck(deck: Deck, output_file: Path) -> None:
    Package(deck).write_to_file(output_file)


def main() -> None:
    qa_list = read_csv(csv_file_path)
    my_deck = create_anki_deck(output_deck_name, qa_list)
    export_anki_deck(my_deck, output_file_path)
    logging.info(f"'{output_deck_name}' Anki deck created")

if __name__ == "__main__":
    main()