.PHONY: install test

test:
	. venv/bin/activate; \
	PYTHONPATH=.:${PYTHONPATH} pytest

install:
	@echo "Creating virtual environment and installing dependencies..."
	python3 -m venv venv; \
    . venv/bin/activate; \
    pip install -r requirements.txt;