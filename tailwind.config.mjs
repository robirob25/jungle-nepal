/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
        serif: ['"Newsreader"', 'Georgia', 'serif'],
      },
      colors: {
        jungle: {
          50: '#f1f7f4',
          100: '#deece4',
          200: '#c0dcce',
          300: '#94c4b1',
          400: '#64a68f',
          500: '#109363',
          600: '#0e8354',
          700: '#0c6d46',
          800: '#0a5235',
          900: '#083c27',
          950: '#041d13',
        },
        safari: {
          50: '#faf8f5',
          100: '#f4efe6',
          200: '#e8ddce',
          300: '#d7c4aa',
          400: '#c2a584',
        }
      }
    },
  },
  plugins: [],
};
