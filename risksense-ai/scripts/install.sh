#!/bin/bash
# Script to install RiskSense AI dependencies

set -e

# Example: Update package list and install Python3 and pip
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Install Python dependencies from requirements.txt if it exists
if [ -f requirements.txt ]; then
	pip3 install -r requirements.txt
fi

echo "Installation complete."
# Clean up apt cache to reduce image size (useful for Docker or CI environments)
sudo apt-get clean
sudo rm -rf /var/lib/apt/lists/*

echo "All dependencies installed and system cleaned up."