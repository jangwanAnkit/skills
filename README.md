# Skills Collection

A personal collection of custom skills for OpenCode and other AI coding agents.

## Available Skills

### minimalist-bw-ui
Create minimalist black and white user interfaces — a complete design system with black background, white text, JetBrains Mono font, and brutalist monochrome styling.

**Use cases:**
- Kanban boards with drag-and-drop columns
- Job application forms
- Analytics dashboards with stats and bar charts
- Data tables with sortable columns
- Login pages with OAuth buttons
- Dark theme admin panels

## Installation

```bash
# Install using npx skills (recommended)
npx skills add jangwanAnkit/minimalist-bw-ui

# Or manually copy to your skills directory
cp -r minimalist-bw-ui ~/.agents/skills/
```

## Experimental Tools

These tools are work-in-progress for adapting the skill-creator workflow to work with opencode:

```
tools/
├── eval_review.html        # Template for reviewing trigger eval sets
├── opencode_wrapper.py     # Helper for opencode run -p
└── improve_description.py # Adapted to use opencode instead of claude -p
```

## Creating New Skills

1. Use the `skill-creator` skill to create a new skill
2. Review trigger evaluation with `tools/eval_review.html`
3. Package the skill and add to this repo
4. Install with: `npx skills add jangwanAnkit/<skill-name>`

## Repository Structure

```
skills/
├── README.md
├── minimalist-bw-ui/
│   ├── SKILL.md
│   ├── evals/
│   │   └── evals.json
│   └── minimalist-bw-ui.skill
└── tools/
    └── ... (experimental)
```

## License

MIT