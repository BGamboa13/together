/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/templates/**/*.html',
    './app/**/*.py',
  ],
  darkMode: 'media', // Cambiada a 'media' según las nuevas recomendaciones
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}