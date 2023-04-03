.PHONY: setup
setup: create-venv install-requirements

.PHONY: create-venv
create-venv:
	@echo "Creating virtual environment with python3.10..."
	test -d anki-env || python3.10 -m venv anki-env

.PHONY: install-requirements
install-requirements:
	@echo "Installing requirements..."
	. anki-env/bin/activate && pip install -r requirements.txt