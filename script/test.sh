#!/bin/bash

SCRIPT_DIR=$(dirname "$(realpath "$BASH_SOURCE")")

DATA_DIR="$SCRIPT_DIR/../data/pxmart-data"
REPO_URL="https://github.com/chienniman/pxmart-data.git"
CHROMEDRIVER="$SCRIPT_DIR/../chromedriver.exe"

if [ -d "$DATA_DIR" ]; then
  echo "Data directory exists, pulling latest changes..."
  cd "$DATA_DIR"
  git pull
  cd - 
else
  echo "Data directory does not exist, cloning repository..."
  mkdir -p "$SCRIPT_DIR/../data"
  cd "$SCRIPT_DIR/../data"
  git clone "$REPO_URL"
  cd -
fi

if [ ! -f "$CHROMEDRIVER" ]; then
  echo "chromedriver.exe not found in script directory. Please add it and try again."
  exit 1
fi

TEST_DIR="$SCRIPT_DIR/../test"

echo "Running local_test.py..."
cd $TEST_DIR
python local_test.py
cd -

sleep 3

echo "Running prd_test.py..."
cd $TEST_DIR
python prd_test.py
cd -
