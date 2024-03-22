import csv
import os
import random
from genanki import Deck, Model, Note, Package
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


output_deck_name: str | None = os.environ.get("DECK_NAME")
if output_deck_name is None:
    output_deck_name = "default_deck_name"

# defining path to dirs
data_dir: str = Path("data")
csv_file_path: str = data_dir / f"{output_deck_name}.csv"

deck_dir: str = Path("decks")
output_file_path: str = deck_dir / f"{output_deck_name}.apkg"


def read_csv(file_path: str) -> list[tuple[str, str]]:
    with open(file_path, "r", encoding="utf-8") as csv_file:
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


def export_anki_deck(deck: Deck, output_file: str) -> None:
    Package(deck).write_to_file(output_file)


def main(input_csv: str, output_anki: str, deck_name: str) -> None:
    qa_list = read_csv(input_csv)
    my_deck = create_anki_deck(deck_name, qa_list)
    export_anki_deck(my_deck, output_anki)
    print(f"'{deck_name}' Anki deck created")


if __name__ == "__main__":
    main(csv_file_path, output_file_path, output_deck_name)
