# B&M's Garage Website

Website for the B&M's Garage YouTube channel.

## Quick Start

```bash
# Install dependencies
npm install

# Start development (watches for CSS changes)
npm run dev

# Build CSS once
npm run build
```

Then open `index.html` in your browser.

## Tech Stack

- **HTML** - Single page site (`index.html`)
- **Tailwind CSS** - Utility-first CSS framework
- **DaisyUI** - Component library for Tailwind
- **GitHub Pages** - Hosting
- **GitHub Actions** - Automated YouTube data fetching

## Project Structure

```
├── index.html          # The website
├── src/input.css       # Custom CSS
├── dist/output.css     # Compiled CSS (auto-generated)
├── images/             # Images and graphics
├── youtube.json        # YouTube data (auto-updated daily)
├── tailwind.config.js  # Tailwind/theme configuration
└── .github/workflows/  # GitHub automation
```

## New to Web Development?

See [LEARNING.md](LEARNING.md) for a complete beginner's guide covering:
- HTML and CSS basics
- How Tailwind CSS works
- Making changes to this site
- Git and GitHub essentials
- Deploying to GitHub Pages
