# Learning Web Development with This Site

This guide is for beginners who want to understand how this website works and learn web development basics. No prior experience needed!

---

## Table of Contents

1. [The Big Picture](#the-big-picture)
2. [Lesson 1: HTML Basics](#lesson-1-html-basics)
3. [Lesson 2: CSS Basics](#lesson-2-css-basics)
4. [Lesson 3: How This Site Uses Tailwind CSS](#lesson-3-how-this-site-uses-tailwind-css)
5. [Lesson 4: Understanding the Project Files](#lesson-4-understanding-the-project-files)
6. [Lesson 5: Making Changes Locally](#lesson-5-making-changes-locally)
7. [Lesson 6: Git and GitHub Basics](#lesson-6-git-and-github-basics)
8. [Lesson 7: Deploying to GitHub Pages](#lesson-7-deploying-to-github-pages)
9. [Practice Exercises](#practice-exercises)
10. [Resources for Further Learning](#resources-for-further-learning)

---

## The Big Picture

A website is made of three main technologies:

| Technology | What It Does | Analogy |
|------------|--------------|---------|
| **HTML** | The content and structure | The skeleton/bones |
| **CSS** | The styling and appearance | The skin, clothes, makeup |
| **JavaScript** | The interactivity | The muscles and brain |

This site mainly uses HTML and CSS. There's a small amount of JavaScript for things like loading YouTube video data.

---

## Lesson 1: HTML Basics

HTML (HyperText Markup Language) tells the browser what content to display.

### How HTML Works

HTML uses "tags" to wrap content. Most tags have an opening and closing tag:

```html
<p>This is a paragraph of text.</p>
```

- `<p>` is the opening tag
- `</p>` is the closing tag
- Everything between them is the content

### Common HTML Tags

| Tag | Purpose | Example |
|-----|---------|---------|
| `<h1>` to `<h6>` | Headings (h1 is biggest) | `<h1>Welcome!</h1>` |
| `<p>` | Paragraph | `<p>Some text here.</p>` |
| `<a>` | Link | `<a href="https://youtube.com">YouTube</a>` |
| `<img>` | Image | `<img src="photo.jpg" alt="A photo">` |
| `<div>` | A container/box | `<div>Stuff inside</div>` |
| `<button>` | A clickable button | `<button>Click Me</button>` |

### HTML Structure

Every HTML page has this basic structure:

```html
<!DOCTYPE html>
<html>
  <head>
    <!-- Info about the page (title, styles, etc.) -->
    <title>My Page</title>
  </head>
  <body>
    <!-- The visible content goes here -->
    <h1>Hello World!</h1>
  </body>
</html>
```

### Try It Yourself

1. Open `index.html` in this project
2. Find the `<body>` tag
3. Look for familiar tags like `<h1>`, `<p>`, `<img>`, and `<a>`
4. Notice how tags can be nested inside other tags

---

## Lesson 2: CSS Basics

CSS (Cascading Style Sheets) controls how things look.

### How CSS Works

CSS has this format:

```css
selector {
  property: value;
}
```

For example:

```css
h1 {
  color: red;
  font-size: 32px;
}
```

This makes all `<h1>` headings red and 32 pixels tall.

### Common CSS Properties

| Property | What It Does | Example Values |
|----------|--------------|----------------|
| `color` | Text color | `red`, `#22C55E`, `rgb(255,0,0)` |
| `background-color` | Background color | `blue`, `#000000` |
| `font-size` | Text size | `16px`, `2rem` |
| `padding` | Space inside an element | `10px`, `20px 10px` |
| `margin` | Space outside an element | `10px`, `auto` |
| `border` | Border around element | `1px solid black` |

### Three Ways to Add CSS

1. **Inline** (directly on the element):
   ```html
   <p style="color: red;">Red text</p>
   ```

2. **Internal** (in the `<head>` section):
   ```html
   <style>
     p { color: red; }
   </style>
   ```

3. **External** (separate file, recommended):
   ```html
   <link rel="stylesheet" href="styles.css">
   ```

---

## Lesson 3: How This Site Uses Tailwind CSS

Instead of writing traditional CSS, this site uses **Tailwind CSS** - a tool that provides pre-made CSS classes.

### Traditional CSS vs Tailwind

**Traditional way:**
```html
<button class="my-button">Click</button>
```
```css
.my-button {
  background-color: green;
  color: white;
  padding: 10px 20px;
  border-radius: 8px;
}
```

**Tailwind way:**
```html
<button class="bg-green-500 text-white px-5 py-2 rounded-lg">Click</button>
```

With Tailwind, you add classes directly to your HTML. Each class does one thing:
- `bg-green-500` = green background
- `text-white` = white text
- `px-5` = horizontal padding
- `py-2` = vertical padding
- `rounded-lg` = rounded corners

### DaisyUI

This site also uses **DaisyUI**, which adds ready-made components on top of Tailwind:

```html
<button class="btn btn-primary">Click Me</button>
```

Instead of listing many Tailwind classes, `btn btn-primary` gives you a nice styled button automatically.

### Key Files for Styling

| File | Purpose |
|------|---------|
| `src/input.css` | Custom CSS and Tailwind imports |
| `dist/output.css` | The compiled CSS (don't edit this directly) |
| `tailwind.config.js` | Tailwind settings and custom colors |

---

## Lesson 4: Understanding the Project Files

Here's what each file/folder does:

```
bandmgarage/
├── index.html          # The main (and only) webpage
├── src/
│   └── input.css       # Your custom CSS code
├── dist/
│   └── output.css      # Compiled CSS (auto-generated)
├── images/             # Photos and graphics
├── youtube.json        # YouTube data (auto-updated)
├── package.json        # Project settings and scripts
├── tailwind.config.js  # Tailwind configuration
├── node_modules/       # Downloaded tools (don't touch)
└── .github/
    └── workflows/      # Automation scripts
```

### The Important Files

**index.html** - This is the entire website. Open it and you'll see all the content.

**src/input.css** - Custom styles go here. When you run the build command, Tailwind processes this file and creates `dist/output.css`.

**tailwind.config.js** - Defines custom colors, fonts, and theme settings for the site.

---

## Lesson 5: Making Changes Locally

### First-Time Setup

1. **Install Node.js** from https://nodejs.org (download the LTS version)

2. **Open a terminal/command prompt** in the project folder

3. **Install dependencies:**
   ```bash
   npm install
   ```
   This downloads all the tools needed (Tailwind, DaisyUI, etc.)

### Making Changes

1. **Start the development watcher:**
   ```bash
   npm run dev
   ```
   This watches for changes and rebuilds the CSS automatically.

2. **Open index.html in your browser**
   - You can double-click the file, or
   - Right-click and "Open with" your browser

3. **Edit and refresh**
   - Make changes to `index.html` or `src/input.css`
   - Save the file
   - Refresh your browser to see changes

### Example: Change a Heading

1. Open `index.html`
2. Find a heading like `<h2 class="...">Some Title</h2>`
3. Change the text between the tags
4. Save and refresh your browser

### Example: Change a Color

1. Open `tailwind.config.js`
2. Find the `colors` section in `theme`
3. Change a hex color value (like `#22C55E`)
4. Save, then run `npm run build` to rebuild CSS
5. Refresh your browser

---

## Lesson 6: Git and GitHub Basics

**Git** is a tool that tracks changes to your files. **GitHub** is a website that stores your Git projects online.

### Key Concepts

| Term | Meaning |
|------|---------|
| **Repository (repo)** | A project folder tracked by Git |
| **Commit** | A saved snapshot of your changes |
| **Push** | Upload your commits to GitHub |
| **Pull** | Download changes from GitHub |
| **Branch** | A separate version of your code |

### Basic Git Workflow

1. **Make changes** to your files

2. **Stage your changes** (tell Git what to include):
   ```bash
   git add .
   ```

3. **Commit** (save a snapshot with a message):
   ```bash
   git commit -m "Updated the about section"
   ```

4. **Push** (upload to GitHub):
   ```bash
   git push
   ```

### Checking Status

See what's changed:
```bash
git status
```

See recent commits:
```bash
git log --oneline
```

---

## Lesson 7: Deploying to GitHub Pages

GitHub Pages is a free service that hosts your website directly from your GitHub repository.

### How It Works for This Site

1. You push changes to GitHub
2. GitHub Pages automatically serves the files
3. Your site is live at `https://yourusername.github.io/bandmgarage/`

### The Deployment Process

When you push to the `main` branch:
1. GitHub detects the push
2. It looks for `index.html` in the root folder
3. It serves that as your website

There's also an automated workflow (`.github/workflows/fetch-youtube.yml`) that:
- Runs daily
- Fetches latest YouTube data
- Updates `youtube.json` automatically

### Making Your Site Live

1. Make and test your changes locally
2. Commit your changes:
   ```bash
   git add .
   git commit -m "Describe what you changed"
   ```
3. Push to GitHub:
   ```bash
   git push
   ```
4. Wait about 1-2 minutes
5. Visit your GitHub Pages URL to see the changes

---

## Practice Exercises

### Exercise 1: Change Text
1. Open `index.html`
2. Find any paragraph or heading
3. Change the text
4. Save and view in browser

### Exercise 2: Change a Button Color
1. Find a button in `index.html`
2. Look for classes like `btn-primary` or `bg-green-500`
3. Try changing `green` to `blue` or `red`
4. Save and view in browser

### Exercise 3: Add a New Section
1. Find where sections are in `index.html` (look for `<section>` tags)
2. Copy an existing section
3. Paste it and modify the content
4. Save and view in browser

### Exercise 4: Make a Git Commit
1. Make any small change
2. Run `git status` to see the change
3. Run `git add .`
4. Run `git commit -m "My first commit"`
5. Run `git push` to upload

---

## Resources for Further Learning

### Free Courses

- **freeCodeCamp** (freecodecamp.org) - Free full curriculum
- **The Odin Project** (theodinproject.com) - Project-based learning
- **MDN Web Docs** (developer.mozilla.org) - Official documentation

### HTML & CSS

- [MDN HTML Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
- [MDN CSS Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)

### Tailwind CSS

- [Tailwind Documentation](https://tailwindcss.com/docs)
- [DaisyUI Components](https://daisyui.com/components/)

### Git & GitHub

- [GitHub Skills](https://skills.github.com/) - Interactive Git courses
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)

### YouTube Tutorials

Search for "HTML CSS for beginners" - there are many great free tutorials.

---

## Quick Reference Card

### Terminal Commands

| Command | What It Does |
|---------|--------------|
| `npm install` | Download project dependencies |
| `npm run dev` | Watch and rebuild CSS as you work |
| `npm run build` | Build CSS once |
| `git status` | See what files changed |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Save changes with a note |
| `git push` | Upload to GitHub |
| `git pull` | Download latest from GitHub |

### Common Tailwind Classes

| Class | Effect |
|-------|--------|
| `text-white` | White text |
| `bg-green-500` | Green background |
| `p-4` | Padding on all sides |
| `px-4` | Horizontal padding |
| `py-4` | Vertical padding |
| `m-4` | Margin on all sides |
| `rounded` | Rounded corners |
| `flex` | Flexbox container |
| `hidden` | Hide element |
| `text-xl` | Extra large text |

---

Good luck on your web development journey! Start small, make lots of changes, break things, fix them, and have fun learning.
