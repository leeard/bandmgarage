/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./src/**/*.js"],
  theme: {
    extend: {
      screens: {
        'xs': '380px',
      },
      fontFamily: {
        'display': ['Kanit', 'system-ui', 'sans-serif'],
        'body': ['Barlow', 'system-ui', 'sans-serif'],
        'condensed': ['"Barlow Condensed"', 'system-ui', 'sans-serif'],
        'mono': ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
      },
    },
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      {
        bmsgarage: {
          "primary": "#53E52B",
          "primary-content": "#0B0C0B",
          "secondary": "#009830",
          "secondary-content": "#FFFFFF",
          "accent": "#C9CDD1",
          "accent-content": "#0B0C0B",
          "neutral": "#1F231D",
          "neutral-content": "#F2F4F1",
          "base-100": "#0B0C0B",
          "base-200": "#141614",
          "base-300": "#1D201D",
          "base-content": "#F2F4F1",
          "info": "#38BDF8",
          "success": "#34D399",
          "warning": "#FACC15",
          "error": "#F87171",
        },
      },
      {
        "bmsgarage-light": {
          "primary": "#097229",
          "primary-content": "#FFFFFF",
          "secondary": "#0B5E22",
          "secondary-content": "#FFFFFF",
          "accent": "#9EA4AA",
          "accent-content": "#FFFFFF",
          "neutral": "#1F231D",
          "neutral-content": "#F2F4F1",
          "base-100": "#F3F4F2",
          "base-200": "#FFFFFF",
          "base-300": "#E7EAE6",
          "base-content": "#161A15",
          "info": "#0284C7",
          "success": "#047857",
          "warning": "#B45309",
          "error": "#DC2626",
        },
      },
    ],
  },
}
