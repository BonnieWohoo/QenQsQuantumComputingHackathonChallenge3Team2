/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './{html,js}', // Adjust the path to your files
  ],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
}
