#!/bin/bash
echo "Runpod llm-backend: Pod started"

SCRIPTDIR=/root/scripts
VOLUME=/workspace
WORKDIR=/app

# If a volume is already defined, $VOLUME will already exist
# If a volume is not being used, we'll still use /app to ensure everything is in a known place.
mkdir -p $VOLUME/logs
mkdir -p $VOLUME/models

# Start build of llama-cpp-python
if [[ ! -f "$VOLUME/.built.llama-cpp-python" ]]; then
  echo "Building llama-cpp-python"
	"$SCRIPTDIR"/build-llama-cpp-python.sh "$VOLUME" >>$VOLUME/logs/build-llama-cpp-python.log 2>&1
else
  echo "Skipping llama-cpp-python build"
fi

if [[ $PUBLIC_KEY ]]; then
  echo "Saving public key"
	mkdir -p ~/.ssh
	chmod 700 ~/.ssh
	cd ~/.ssh
	echo "$PUBLIC_KEY" >>authorized_keys
	chmod 700 -R ~/.ssh
	service ssh start
fi

MODEL_NAME=""

# If passed a MODEL variable from Runpod template, start it downloading
# This will block the UI until completed
# MODEL can be a HF repo name, eg 'TheBloke/guanaco-7B-GPTQ'
# or it can be a direct link to a single GGML file, eg 'https://huggingface.co/TheBloke/tulu-7B-GGML/resolve/main/tulu-7b.ggmlv3.q2_K.bin'
if [[ $MODEL ]]; then
  MODEL_NAME=$(basename "$MODEL")

  if [[ -f "$VOLUME/models/$MODEL_NAME" ]]; then
      echo "$MODEL_NAME exists, skipping download..."
  else
    echo "Fetching model $MODEL"
	  "$SCRIPTDIR"/fetch-model.py "$MODEL" $VOLUME/models >>$VOLUME/logs/fetch-model.log 2>&1
	fi
fi

# Use the downloaded model of the first *.bin model file
if [[ $MODEL_NAME == "" ]]; then
  FILE=$(find "$VOLUME/models" -name "*.bin" | head -n 1)
else
  FILE="$VOLUME/models/$MODEL_NAME"
fi

# Env. variables for our server
export LOG_LEVEL="DEBUG"
export LLAMA_MODEL_FILE="$FILE"
export LLAMA_CONTEXT_SIZE="${LLAMA_CONTEXT_SIZE:-4096}"
export OPENAI_API_KEY="$OPENAI_API_KEY"

echo "Launching gunicorn server"
echo "- Log level: $LOG_LEVEL"
echo "- Model file: $LLAMA_MODEL_FILE"
echo "- Context size: $LLAMA_CONTEXT_SIZE"
echo "- OpenAI API key: ...${OPENAI_API_KEY: -4}"
gunicorn -b :5000 \
  --chdir "$WORKDIR" \
  --log-level debug \
  --access-logfile $VOLUME/logs/gunicorn-access.log \
  --error-logfile $VOLUME/logs/gunicorn-error.log \
  server:flask_app \
  --timeout 120

# If we get here, gunicorn has exited
# Gives us a chance to debug the container
echo "Runpod llm-backend: Pod exited"
sleep infinity