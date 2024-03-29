# Generating Custom Anki Decks with Python, GPT4, and LangChain

This guide will take you through the steps to create custom Anki decks using Python, GPT4, and LangChain.

## Installation and Setup

1. Open the `.env.example` file, rename it to `.env` and add the following information:

   - Name of your Anki deck
   - Your OpenAI API key

2. Install the core dependencies:
   ```
   poetry install --without dev
   ```
   Alternatively if you don't have Poetry installed, use the following command and execute the `.py` files directly
   ```
   python3.11 -m venv venv && \
   source venv/bin/activate && \
   pip install -r requirements.txt
   ```

## Usage

1. Paste the text from which you want to create Anki cards into the `input.txt` file

2. To generate flashcards in CSV format:

   ```shell
   poetry run generate-flashcards
   ```

   This will automatically generate a CSV file. If you wish to create additional cards, simply add new text into the `input.txt` file and rerun the `generate-flashcards` command. It will append the new cards to the existing CSV.

3. Convert the CSV file to an Anki deck using the following command:

   ```shell
   poetry run generate-deck
   ```

4. The Anki deck will be created in the `decks` directory

5. Open the Anki app and import the deck using the app's import function

## For Contributors

If you're interested in modifying or contributing to the project, follow these additional steps to set up your development environment:

1. Install all dependencies, including those required for development:

   ```shell
   poetry install
   ```

2. Run tests and linting to ensure your modifications don't break existing functionality:

   ```shell
   poetry run nox
   ```

   This command runs predefined Nox sessions, which include running ruff and mypy as defined in the `noxfile.py`
