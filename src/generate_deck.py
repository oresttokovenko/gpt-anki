import csv
import genanki
import sys
import os
import random
from dotenv import load_dotenv

load_dotenv("../.env")
output_deck_name = os.environ.get("DECK_NAME")
csv_file_path = "../csv/" + output_deck_name + ".csv"
output_file_path = "../decks/" + output_deck_name + ".apkg"

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        qa_list = [(row[0], row[1]) for row in csv_reader]
    return qa_list

def create_anki_deck(deck_name, qa_list):
    model_id = random.randrange(1 << 30, 1 << 31)
    my_model = genanki.Model(
        model_id,
        'Simple Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])

    deck_id = random.randrange(1 << 30, 1 << 31)
    my_deck = genanki.Deck(deck_id, deck_name)

    for question, answer in qa_list:
        my_note = genanki.Note(model=my_model, fields=[question, answer])
        my_deck.add_note(my_note)

    return my_deck

def export_anki_deck(deck, output_file):
    genanki.Package(deck).write_to_file(output_file)

def main(input_csv, output_anki, deck_name):
    qa_list = read_csv(input_csv)
    my_deck = create_anki_deck(deck_name, qa_list)
    export_anki_deck(my_deck, output_anki)
    print(f"Anki deck '{deck_name}' created")

if __name__ == '__main__':
    main(csv_file_path, output_file_path, output_deck_name)