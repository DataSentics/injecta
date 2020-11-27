#!/bin/bash -e

CONDA_BASE_DIR=$(conda info --base | sed 's/\\/\//g')

if [ -d "$CONDA_BASE_DIR/Scripts" ]; then
CONDA_BIN_DIR="$CONDA_BASE_DIR/Scripts" # Windows
else
CONDA_BIN_DIR="$CONDA_BASE_DIR/bin" # Linux/Mac
fi

$CONDA_BIN_DIR/pip install "penvy>=1.0.0"
$CONDA_BIN_DIR/penvy-init "$@"
