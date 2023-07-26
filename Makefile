.PHONY: install test

test:
	. venv/bin/activate; \
	PYTHONPATH=.:${PYTHONPATH} pytest -v

install:
	@echo "Creating virtual environment and installing dependencies..."
	python3 -m venv venv; \
    . venv/bin/activate; \
    LLAMA_METAL=1 pip install -r requirements.txt;

run:
	@echo "Running local server..."
	. venv/bin/activate; \
	python3 server.py;