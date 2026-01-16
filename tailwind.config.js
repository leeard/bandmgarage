/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./src/**/*.js"],
  theme: {
    extend: {
      fontFamily: {
        'display': ['"Bebas Neue"', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      {
        bmsgarage: {
          "primary": "#22C55E",
          "secondary": "#16A34A",
          "accent": "#86EFAC",
          "neutral": "#1f2937",
          "base-100": "#0a0a0a",
          "base-200": "#141414",
          "base-300": "#1f1f1f",
          "info": "#22D3EE",
          "success": "#34D399",
          "warning": "#FBBF24",
          "error": "#F87171",
        },
      },
      {
        "bmsgarage-light": {
          "primary": "#16A34A",
          "secondary": "#15803D",
          "accent": "#166534",
          "neutral": "#1f2937",
          "base-100": "#ffffff",
          "base-200": "#f3f4f6",
          "base-300": "#e5e7eb",
          "info": "#0891B2",
          "success": "#059669",
          "warning": "#D97706",
          "error": "#DC2626",
        },
      },
    ],
  },
}
