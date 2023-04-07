# How to Use Python and ChatGPT to Generate Custom Anki Decks

Follow these instructions to create custom Anki decks using Python and ChatGPT:

### Prerequisites and Installation

1. Install Anki if you don't already have it
```
brew install anki
```
2. Clone this GitHub repository.
3. Ensure your OpenAI API key is added to your .bashrc or .zshrc file

### Usage

1. Navigate to the root directory of the cloned repository
2. Run the Make file
```
make setup
```
3. Edit the `gpt.py` file - Replace the `input` variable with the text you want to convert into flashcards
4. Run `gpt.py` to generate flashcards in CSV format:
```
python src/gpt.py
```
 The output will be displayed in the command line
 5. opy the generated output and paste it into the `csv/java_decks.csv` file. You can rename this file or create a new CSV file to organize your decks
 6. Convert the CSV file to an Anki deck:
```
python csv_to_anki.py csv/java_decks.csv decks/java.anki
```
7. Copy the generated `java.anki` file to your Desktop
8. Open the Anki app and import the deck
9. Enjoy your custom Anki deck!

### Best Practices

* Organize your flashcards by topic, and create separate CSV files for each topic
* Keep your API key secure by storing it in an environment variable or using a secrets manager
* Regularly update your Anki decks to keep your learning materials fresh and relevant