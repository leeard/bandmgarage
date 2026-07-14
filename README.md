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
- **GitHub Pages** - Hosting at https://leeard.github.io/bandmgarage/
- **GitHub Actions** - Daily YouTube data fetch (hands-off)

## Hands-off sections (daily job)

`youtube.json` is refreshed every day by `.github/workflows/fetch-youtube.yml`. The page reads it at load:

| Section | Source |
|---|---|
| Latest + video grid | Recent long-form uploads |
| Shorts | Channel Shorts playlist |
| Stats | Channel subscriber / video / view counts |
| Gear | Product links (`amazon.com/dp`, `a.co`, `amzn.to`, `geni.us`) in descriptions |
| Deals | Partner URLs from the latest long-form description (codes stay in `PARTNER_META` in `index.html`) |

Manual trigger:

```bash
gh workflow run fetch-youtube.yml
```

Only edit `index.html` for static copy (About, Contact, partner **codes**). Video rails and links refresh themselves.

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
