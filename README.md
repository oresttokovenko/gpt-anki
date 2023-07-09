# Generating Custom Anki Decks with Python, GPT4, and LangChain

This guide will take you through the steps to create custom Anki decks using Python, GPT4, and LangChain.

## Prerequisites

Before getting started, please ensure the following:

1. Anki is installed on your system. If not, use the following command to install Anki:
   ```shell
   brew install anki
   ```

2. You have cloned this GitHub repository onto your local machine.

3. You have your OpenAI API key ready for usage.

## Installation and Setup

1. Navigate to the root directory of the cloned repository.

2. Setup the necessary dependencies by running the Make file:
   ```shell
   make setup
   ```

3. Open the `.env` file and add the following information:
   - Name of your Anki deck.
   - Your OpenAI API key.

## Usage

Follow these steps to generate flashcards and convert them into an Anki deck:

1. Paste the text from which you want to create Anki cards into the `input.txt` file.

2. Run the `generate_flashcards.py` script to generate flashcards in CSV format:
   ```shell
   python src/generate_flashcards.py
   ```
   This will automatically generate a CSV file. If you wish to create additional cards, simply add new text into the `input.txt` file and rerun the `generate_flashcards.py` script. It will append the new cards to the existing CSV.

3. Convert the CSV file to an Anki deck using the `generate_deck.py` script:
   ```shell
   python src/generate_deck.py
   ```

4. The Anki deck will be created in the `csv` directory. 

5. Open the Anki app and import the deck using the app's import function.