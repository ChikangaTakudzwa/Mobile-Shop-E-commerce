echo "....................."
echo "....................."
echo "Installing htmx"
echo "....................."
echo "....................."
npm install htmx.org

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


