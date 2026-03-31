---
name: minimalist-bw-ui
description: |
  Create minimalist black and white user interfaces — a complete design system with black background, white text, JetBrains Mono font, and brutalist monochrome styling. Use whenever building: kanban boards with drag-and-drop columns, job application forms with fields for company/position/salary, analytics dashboards with stats and bar charts, data tables with sortable columns, login pages with OAuth buttons (Google/GitHub), dark theme admin panels, or any UI needing the "job tracker style". Trigger phrases: "design like job tracker", "minimalist black white UI", "monochrome design", "dark theme interface", "terminal-style UI", "brutalist interface", "jetbrains mono font", "bento grid layout", "recreate this UI".
---

# Minimalist Black & White UI Design System

A design system for creating clean, minimalist interfaces using a black and white color palette. This system is inspired by the JobTracker application — a sleek, terminal-inspired UI using JetBrains Mono font with a stark black background and white text.

## When to Use This Design System

Use this skill whenever you're building any user interface that should:
- Have a minimalist, monochrome aesthetic
- Feel technical/developer-oriented
- Use JetBrains Mono or similar monospace font
- Feature clean data presentation (tables, forms, dashboards)
- Include kanban boards or drag-and-drop interfaces

## Design System Foundation

### Color Palette

```css
:root {
    --bg: #000;           /* Primary background - always black */
    --fg: #fff;           /* Primary foreground - always white */
    --muted: #888;        /* Secondary text, labels */
    --border: #333;       /* Borders, dividers */
    
    /* Status colors for job tracking (optional accent) */
    --status-saved: #888;
    --status-applied: #0ff;
    --status-assessment: #ff0;
    --status-interview: #f0f;
    --status-offer: #0f0;
    --status-rejected: #f00;
    --status-ghosted: #555;
    --status-archived: #333;
}
```

### Typography

- **Font Family**: `'JetBrains Mono', monospace`
- **Font Sizes**:
  - Brand/Headers: 18px, weight 700, uppercase
  - Section Headers: 11-13px, uppercase, weight 400-700
  - Body: 13px
  - Labels: 11px, uppercase
  - Meta/Small: 11-12px
- **Line Height**: 1.5

### Spacing System

- Base unit: 0.25rem (4px)
- Common spacings: 0.25rem, 0.5rem, 0.75rem, 1rem, 2rem
- Padding: 0.4rem 0.5rem for inputs/buttons
- Margins: 0.5rem-1rem between sections

### Layout Principles

1. **Single column content** with max-width ~900px for readability
2. **Card-based layouts** using 1px solid borders
3. **Grid systems**: CSS Grid for kanban (7 cols desktop, 4 tablet, 1 mobile)
4. **Flexbox** for nav, filters, form fields
5. **Responsive breakpoints**: 1200px, 768px

---

## Core Components

### Navigation

```html
<nav>
    <span class="brand">APP NAME</span>
    <div class="nav-links">
        <a href="/page1">PAGE1</a>
        <a href="/page2">PAGE2</a>
    </div>
</nav>
```

**CSS:**
```css
nav {
    display: flex;
    align-items: center;
    gap: 2rem;
    padding: 0.5rem 1rem;
    border-bottom: 1px solid var(--border);
    text-transform: uppercase;
    font-size: 12px;
}

nav .brand {
    font-weight: 700;
    margin-right: auto;
}

nav a.active {
    text-decoration: underline;
}

.link-button {
    background: none;
    border: none;
    color: var(--fg);
    font-family: inherit;
    font-size: inherit;
    text-transform: uppercase;
    cursor: pointer;
    padding: 0;
}

.link-button:hover {
    text-decoration: underline;
}
```

### Buttons

```html
<button>PRIMARY ACTION</button>
<a class="social-btn">SECONDARY</a>
```

**CSS:**
```css
button {
    background: var(--fg);
    color: var(--bg);
    border: 1px solid var(--fg);
    padding: 0.4rem 0.5rem;
    font-family: inherit;
    font-size: inherit;
    text-transform: uppercase;
    cursor: pointer;
}

.social-btn {
    display: block;
    text-align: center;
    padding: 0.5rem;
    border: 1px solid var(--fg);
    color: var(--fg);
    text-decoration: none;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.social-btn:hover {
    background: var(--fg);
    color: var(--bg);
}
```

### Form Fields

```html
<div class="form-field">
    <label for="field">FIELD LABEL</label>
    <input type="text" id="field" placeholder="Placeholder">
</div>

<select>
    <option>Option 1</option>
</select>

<textarea></textarea>
```

**CSS:**
```css
.form-field {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
}

.form-field label {
    font-size: 11px;
    color: var(--muted);
    text-transform: uppercase;
}

input, select, textarea {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--fg);
    padding: 0.4rem 0.5rem;
    font-family: inherit;
    font-size: inherit;
}

input:focus, select:focus, textarea:focus {
    outline: none;
    border-color: var(--fg);
}

select option {
    background: #000;
    color: #fff;
}
```

### Data Tables

```html
<table>
    <thead>
        <tr>
            <th>COLUMN 1</th>
            <th>COLUMN 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Data 1</td>
            <td>Data 2</td>
        </tr>
    </tbody>
</table>
```

**CSS:**
```css
table {
    width: 100%;
    border-collapse: collapse;
}

th {
    text-transform: uppercase;
    font-size: 11px;
    color: var(--muted);
    font-weight: 400;
    text-align: left;
    padding: 0.5rem 0.25rem;
    border-bottom: 1px solid var(--border);
}

td {
    padding: 0.5rem 0.25rem;
    border-bottom: 1px solid var(--border);
    font-size: 13px;
}

tr a {
    color: var(--fg);
    text-decoration: none;
}
```

### Status Badges

```html
<span class="status status-applied">APPLIED</span>
```

**CSS:**
```css
.status {
    text-transform: uppercase;
    font-size: 11px;
    padding: 2px 6px;
    border: 1px solid currentColor;
    display: inline-block;
}

.status-saved { color: var(--status-saved); }
.status-applied { color: var(--status-applied); }
.status-assessment { color: var(--status-assessment); }
.status-interview { color: var(--status-interview); }
.status-offer { color: var(--status-offer); }
.status-rejected { color: var(--status-rejected); }
.status-ghosted { color: var(--status-ghosted); }
.status-archived { color: var(--status-archived); }
```

### Kanban Board

```html
<div class="kanban-board">
    <div class="kanban-column" data-status="applied">
        <h2>APPLIED (5)</h2>
        <div class="kanban-card">
            <div class="card-title">Job Title</div>
            <div class="card-company">Company</div>
            <div class="card-meta">$100k • Remote</div>
        </div>
    </div>
</div>
```

**CSS:**
```css
.kanban-board {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 1rem;
}

@media (max-width: 1200px) {
    .kanban-board {
        grid-template-columns: repeat(4, 1fr);
    }
}

@media (max-width: 768px) {
    .kanban-board {
        grid-template-columns: 1fr;
    }
}

.kanban-column h2 {
    font-size: 11px;
    color: var(--muted);
    text-transform: uppercase;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 0.5rem;
    font-weight: 400;
}

.kanban-card {
    border: 1px solid var(--border);
    padding: 0.5rem;
    margin-bottom: 4px;
    cursor: grab;
    display: block;
    color: var(--fg);
    text-decoration: none;
}

.kanban-card .card-title {
    font-weight: 700;
    font-size: 13px;
}

.kanban-card .card-company {
    font-size: 12px;
}

.kanban-card .card-meta {
    font-size: 11px;
    color: var(--muted);
}
```

### Stats Dashboard

```html
<div class="stats">
    <div class="stat">
        <div class="stat-label">TOTAL</div>
        <div class="stat-value">42</div>
    </div>
    <div class="stat">
        <div class="stat-label">RATE</div>
        <div class="stat-value">75%</div>
    </div>
</div>
```

**CSS:**
```css
.stats {
    display: flex;
    gap: 3rem;
    margin-bottom: 2rem;
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid var(--border);
}

.stat .stat-value {
    font-size: 20px;
    font-weight: 700;
}

.stat .stat-label {
    font-size: 11px;
    color: var(--muted);
    text-transform: uppercase;
}
```

### Charts Container

```html
<div class="charts">
    <div class="chart-container">
        <h3>CHART TITLE</h3>
        <canvas id="chart"></canvas>
    </div>
</div>
```

**CSS:**
```css
.charts {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    max-width: 900px;
}

@media (max-width: 768px) {
    .charts {
        grid-template-columns: 1fr;
    }
}

.chart-container h3 {
    font-size: 11px;
    color: var(--muted);
    text-transform: uppercase;
    margin-bottom: 1rem;
    font-weight: 400;
}

/* Chart.js configuration for monochrome */
Chart.defaults.color = '#888';
Chart.defaults.borderColor = '#333';
Chart.defaults.font.family = "'JetBrains Mono', monospace";
Chart.defaults.font.size = 11;
```

### Filters Bar

```html
<div class="filters">
    <select>Filter 1</select>
    <select>Filter 2</select>
    <input type="search" placeholder="SEARCH...">
</div>
```

**CSS:**
```css
.filters {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
    align-items: center;
}
```

---

## Example Page Templates

### Login Page

```html
<div class="login-container">
    <h1>LOGIN</h1>
    <hr>
    <div class="social-login">
        <a href="/auth/google" class="social-btn">GOOGLE</a>
        <a href="/auth/github" class="social-btn">GITHUB</a>
    </div>
    <form>
        <div class="form-field">
            <label>EMAIL</label>
            <input type="email" name="email">
        </div>
        <div class="form-field">
            <label>PASSWORD</label>
            <input type="password" name="password">
        </div>
        <button type="submit">SIGN IN</button>
    </form>
</div>
```

### Job Application Form

```html
<form class="job-form">
    <div class="form-field">
        <label for="title">JOB TITLE</label>
        <input type="text" id="title" name="title">
    </div>
    <div class="form-field">
        <label for="company">COMPANY</label>
        <input type="text" id="company" name="company">
    </div>
    <div class="form-field">
        <label for="status">STATUS</label>
        <select id="status" name="status">
            <option value="saved">SAVED</option>
            <option value="applied">APPLIED</option>
            <option value="assessment">ASSESSMENT</option>
            <option value="interview">INTERVIEW</option>
            <option value="offer">OFFER</option>
            <option value="rejected">REJECTED</option>
            <option value="ghosted">GHOSTED</option>
        </select>
    </div>
    <div class="form-field">
        <label for="salary">SALARY</label>
        <input type="text" id="salary" name="salary">
    </div>
    <div class="form-field">
        <label for="location">LOCATION</label>
        <input type="text" id="location" name="location">
    </div>
    <div class="form-field">
        <label for="url">JOB URL</label>
        <input type="url" id="url" name="url">
    </div>
    <div class="form-field">
        <label for="notes">NOTES</label>
        <textarea id="notes" name="notes" rows="4"></textarea>
    </div>
    <button type="submit">SAVE</button>
</form>
```

### Job Detail Page

```html
<div class="job-header">
    <h1>SOFTWARE ENGINEER</h1>
    <div class="job-meta">
        <span>ACME CORP</span>
        <span class="status status-interview">INTERVIEW</span>
        <span>$120k • San Francisco, CA</span>
    </div>
</div>

<dl class="job-info">
    <dt>URL</dt>
    <dd><a href="...">Job Posting</a></dd>
    <dt>SOURCE</dt>
    <dd>LinkedIn</dd>
    <dt>APPLIED</dt>
    <dd>2024-01-15</dd>
    <dt>NOTES</dt>
    <dd>Interesting opportunity...</dd>
</dl>

<div class="section-header">ACTIVITY LOG</div>
<div class="activity-list">
    <div class="activity-item">
        <span class="activity-date">2024-01-20</span>
        <span class="activity-type">STATUS CHANGE</span>
        <span>Moved to Interview</span>
    </div>
</div>
```

---

## Responsive Behavior

Always include these media queries:

```css
@media (max-width: 1200px) {
    .kanban-board {
        grid-template-columns: repeat(4, 1fr);
    }
}

@media (max-width: 768px) {
    .kanban-board {
        grid-template-columns: 1fr;
    }
    .charts {
        grid-template-columns: 1fr;
    }
    nav {
        flex-wrap: wrap;
        gap: 1rem;
    }
    .job-meta {
        flex-direction: column;
        gap: 0.5rem;
    }
}
```

---

## Implementation Checklist

When building UI with this design system, ensure:

1. [ ] Black background (`--bg: #000`) on body
2. [ ] White text (`--fg: #fff`) on body
3. [ ] JetBrains Mono font loaded from Google Fonts
4. [ ] All text is uppercase for headers, labels, navigation
5. [ ] 1px solid border (`--border: #333`) on cards, tables, inputs
6. [ ] 11px uppercase labels with `--muted` color
7. [ ] Button uses inverted colors (white bg, black text)
8. [ ] Form inputs have transparent background
9. [ ] Focus states use `--fg` border color
10. [ ] Include Chart.js defaults config for monochrome charts
11. [ ] Use CSS Grid for kanban with responsive breakpoints
12. [ ] Status badges use colored text with 1px border
13. [ ] Include mobile breakpoints at 768px

---

## Technology-Agnostic Notes

- **CSS Variables**: The design system uses CSS custom properties which work in any modern framework
- **HTML Structure**: Semantic HTML works with any templating (Django, Jinja2, React, Vue, etc.)
- **Charts**: Chart.js configuration shown — adapt to your charting library
- **Drag & Drop**: SortableJS configuration shown — adapt to your framework's DnD solution
- **HTMX Compatible**: The filters and forms work seamlessly with HTMX for progressive enhancement