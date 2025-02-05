#!/bin/bash

DATA_DIR="./data/pxmart-data"
REPO_URL="https://github.com/chienniman/pxmart-data.git"
CHROMEDRIVER="./chromedriver.exe"

if [ -d "$DATA_DIR" ]; then
  echo "Data directory exists, pulling latest changes..."
  cd "$DATA_DIR"
  git pull
  cd - 
else
  echo "Data directory does not exist, cloning repository..."
  mkdir -p ./data
  cd ./data
  git clone "$REPO_URL"
  cd -
fi

if [ ! -f "$CHROMEDRIVER" ]; then
  echo "chromedriver.exe not found in root directory. Please add it and try again."
  exit 1
fi

echo "Running local_test.py..."
python local_test.py

sleep 3

echo "Running prd_test.py..."
python prd_test.py
