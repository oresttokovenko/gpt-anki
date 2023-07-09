.PHONY: setup create-virtualenv install-requirements clean freeze-requirements

# setup: creates a virtual environment and installs requirements
setup: create-virtualenv install-requirements create-env

# create-virtualenv: creates a new virtual environment using Python 3.10
create-virtualenv:
	@echo "Creating virtual environment with python3.10..."
	test -d anki-env || python3.10 -m venv anki-env

# install-requirements: activates the virtual environment and installs the required packages
install-requirements:
	@echo "Installing requirements..."
	. anki-env/bin/activate && pip install -r requirements.txt

# create-env: creates a .env file in the root directory for storing your api key
create-env:
	@echo "Creating .env for api key and deck name"
	@touch .env
	@echo "DECK_NAME=" >> .env
	@echo "OPENAI_API_KEY=" >> .env

# clean: removes the virtual environment directory
clean:
	@echo "Cleaning up virtual environment..."
	rm -rf anki-env

# freeze-requirements: generates a requirements.txt file based on the installed packages
freeze-requirements:
	@echo "Freezing requirements..."
	. anki-env/bin/activate && pip freeze > requirements.txt
