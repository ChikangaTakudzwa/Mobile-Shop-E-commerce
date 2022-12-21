#!/bin/bash
echo "****************************************"
echo " Setting up Environment"
echo " Python 3.8"
echo " Ubuntu 20."
echo "****************************************"

echo "Updating package manager..."
sudo add-apt-repository -y ppa:deadsnakes/ppa

echo "Installing Python 3.8 and Virtual Environment"
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3.8 python3.8-venv

echo "Creating a Python virtual environment"
python3.8 -m venv appenv

echo "Checking the Python version..."
python3 --version

echo "Installing Python depenencies..."
source appenv/bin/activate && python3 -m pip install --upgrade pip wheel
source appenv/bin/activate && pip install -r ./project/requirements.txt

echo="Adding postcss and autoprefixer"
cd project && yarn add -W tailwindcss@latest postcss@latest autoprefixer@latest

echo "Installing Tailwind"
cd project && npm install -D tailwindcss

echo "Running Tailwind init"
cd project && npx tailwindcss init

echo "installing flowbite"
cd project && npm i flowbite

echo "Watching tailwind css"
cd project && npx tailwindcss -i ./app/static/css/input.css -o ./app/static/css/output.css --watch



echo "****************************************"
echo " Environment Setup Complete"
echo "****************************************"
echo ""
echo "Use source appenv/bin/activate to activate virtual env"
echo ""