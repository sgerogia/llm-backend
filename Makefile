.PHONY: install test

CHATBOT_UI_FOLDER := '../chatbot-ui'

BACKEND_BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
UI_BRANCH := $(shell cd ${CHATBOT_UI_FOLDER} && git rev-parse --abbrev-ref HEAD)

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
	pip install gunicorn; \
	gunicorn -b :5000 --log-level debug --access-logfile - --error-logfile - server:flask_app;


build-docker:
	@echo "Building Docker images. Requires `docker login`"

	@echo "\t---> Chatbot UI"
	cd ${CHATBOT_UI_FOLDER}; \
	docker build -t sgerogia/chatbot-ui:${UI_BRANCH} .; \
	docker push sgerogia/chatbot-ui:${UI_BRANCH}

	@echo "\t---> LLM Backend - CUDA"
	docker build -t sgerogia/llm-backend:${BACKEND_BRANCH}-cuda . -f ./Dockerfile.runpod; \
	docker push sgerogia/llm-backend:${BACKEND_BRANCH}-cuda

	# The following requires the Mac OS SDK to be present in order to work
#	@echo "\t---> LLM Backend - Metal"
#	docker build --build-arg CMAKE_ARGS="-DLLAMA_METAL=on" -t sgerogia/llm-backend:${BACKEND_BRANCH}-metal .; \
#	docker push sgerogia/llm-backend:${BACKEND_BRANCH}-metal

