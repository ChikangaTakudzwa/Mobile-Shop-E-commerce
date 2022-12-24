/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './project/app/templates/**/*.html',
    './project/product/templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin'),
    require('flowbite-typography'),
  ],
}
