#!/bin/bash

VOLUME="$1"  # Capture the first argument passed to the script

# Install llama-cpp-python with GPU acceleration, overwriting the version installed by llm-backend
# We do this on boot, so as to ensure the binaries are built with the right CPU instructions for the machine being used

# Uninstall llama-cpp-python, which will have been auto installed by llm-backend's requirements.txt
echo "Uninstalling llama-cpp-python"
pip3 uninstall -qy llama-cpp-python

# Check to see if this machine supports AVX2 instructions
if python3 /root/scripts/check_avx2.py; then
  echo "AVX2 supported"
  export CMAKE_ARGS="-DLLAMA_CUBLAS=on -DCMAKE_CUDA_COMPILER=/usr/local/cuda/bin/nvcc"
else
  # If it does not, we need to specifically tell llama-cpp-python not to use them
  # as unfortunately it's otherwise hardcoded to use them
  echo "AVX2 not supported"
  export CMAKE_ARGS="-DLLAMA_AVX2=OFF -DLLAMA_CUBLAS=on -DCMAKE_CUDA_COMPILER=/usr/local/cuda/bin/nvcc"
fi

export PATH=/usr/local/cuda/bin:"$PATH"
export FORCE_CMAKE=1

echo "Building llama-cpp-python"
if pip3 install --no-cache-dir llama-cpp-python; then
  # touch this file so we don't build again on reboots
  touch "${VOLUME}/.built.llama-cpp-python"
fi