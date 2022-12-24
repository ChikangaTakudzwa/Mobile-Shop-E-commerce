#!/bin/bash
echo "****************************************"
echo " Setting up Environment"
echo " Python 3.8"
echo " Ubuntu 20."
echo "****************************************"

echo "Updating package manager..."
echo "....................."
echo "....................."
sudo add-apt-repository -y ppa:deadsnakes/ppa

echo "Installing Python 3.8 and Virtual Environment"
echo "....................."
echo "....................."
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3.8 python3.8-venv

echo "Creating a Python virtual environment"
echo "....................."
echo "....................."
python3.8 -m venv appenv

echo "Checking the Python version..."
echo "....................."
echo "....................."
python3 --version

echo "Installing Python depenencies..."
echo "....................."
echo "....................."
source appenv/bin/activate && python3 -m pip install --upgrade pip wheel
source appenv/bin/activate && pip install -r ./project/requirements.txt

echo "....................."
echo "....................."
echo "Adding postcss and autoprefixer"
echo "....................."
echo "....................."
yarn add -W tailwindcss@latest postcss@latest autoprefixer@latest

echo "....................."
echo "....................."
echo "Installing Tailwind"
echo "....................."
echo "....................."
npm install -D tailwindcss

echo "....................."
echo "....................."
echo "Running Tailwind init"
echo "....................."
echo "....................."
npx tailwindcss init

echo "....................."
echo "....................."
echo "installing flowbite"
echo "....................."
echo "....................."
npm i flowbite

echo "....................."
echo "....................."
echo "installing flowbite-typography"
echo "....................."
echo "....................."
npm install -D flowbite-typography

echo "....................."
echo "....................."
echo "Watching tailwind css"
echo "....................."
echo "....................."

npx tailwindcss -i ./project/app/static/css/input.css -o ./project/app/static/css/output.css --watch



echo "****************************************"
echo " Environment Setup Complete"
echo "****************************************"
echo ""
echo "Use source appenv/bin/activate to activate virtual env"
echo ""