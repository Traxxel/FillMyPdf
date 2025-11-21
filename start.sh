#!/bin/bash

# Navigate to the python directory
cd "$(dirname "$0")/python" || exit

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Please run setup first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Run the application
echo "Starting Python PDF Processing Service..."
python src/app.py
