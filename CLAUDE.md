# Strategy Blog Agents

This project runs two AI agents that collaborate on strategy research throughout the week,
then compile their discussion into a polished blog post every Sunday.

## How it works

1. **Research file**: `research/week-YYYY-MM-DD.md` (dated to Monday of that week)
2. **Agents write to the same file** throughout the week, building on each other
3. **Sunday**: A compiler agent reads the week's discussion and produces `blogs/YYYY-MM-DD-title.md`

## Agent roles

- **R (Researcher)**: Surfaces topics, digs into primary sources, finds non-obvious angles
- **A (Analyst)**: Stress-tests ideas, builds frameworks, sharpens conclusions

## File conventions

- Weekly research files live in `research/`
- Final blogs live in `blogs/`
- Config (topics, style, personalities) in `config.yaml`
- Each agent entry in the research file uses this format:

```
## Day | R | Topic Title
## Day | A | Topic Title
```

**Never use em dashes (—) in entry headers. Always use pipes (`|`).**

## Rules for agents

1. **Always read the full research file first** before adding your entry
2. **Build on what's already there** — reference and respond to previous entries
3. **Pick 1-2 topics per entry** — go deep, not broad
4. **Include sources** when referencing specific data, events, or claims
5. **Challenge each other** — disagreement produces better insights
6. **Keep a running "strongest threads" section** at the top of the file
7. **Use web search** to find current, real information — never fabricate facts
8. **Tag open questions** with `[?]` so the other agent can pick them up
