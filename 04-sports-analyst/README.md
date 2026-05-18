# AI Sports Analyst

Fetches today's NBA games and major European football matches from public APIs, sends the combined list to Claude (via the official Anthropic SDK), and prints a structured, validated daily analysis.

## What it demonstrates

- **Multi-source data integration** — two different sports APIs with different auth schemes (Bearer-style header vs. custom `X-Auth-Token`), unified into a single internal schema.
- **Structured LLM output** — pydantic models define the contract; Anthropic tool-use forces schema-compliant responses from Claude. No fragile string parsing.
- **Clean separation of concerns** — `sports/` does I/O, `analyst.py` does AI, `models.py` defines the schema, `main.py` orchestrates.
- **Timezone-aware date handling** — NBA dates queried in US Eastern, football queried in UTC, matching what each API indexes by.

## Project layout

```
04-sports-analyst/
├── main.py            # entry point — orchestrates fetch -> analyse -> print
├── analyst.py         # Claude integration; returns a validated DayAnalysis
├── models.py          # pydantic models defining the AI's response contract
├── sports/
│   ├── nba.py         # fetches today's NBA games (balldontlie.io)
│   └── football.py    # fetches today's football matches (football-data.org)
├── .env               # API keys (gitignored)
└── pyproject.toml
```

## Running it

```bash
uv run python main.py
```

Requires three environment variables in `.env`:

```
NBA_API_KEY=...           # https://www.balldontlie.io/
FOOTBALL_API_KEY=...      # https://www.football-data.org/
ANTHROPIC_API_KEY=...     # https://console.anthropic.com/
```

## Example output

```
=== Thunder Eyes Form Against Spurs, Arsenal Host Burnley ===

  Oklahoma City Thunder vs San Antonio Spurs (NBA)
    The Thunder look to maintain momentum against the perennial Spurs...

  Arsenal FC vs Burnley FC (Premier League)
    The Gunners welcome Burnley to the Emirates looking to strengthen
    their title push...

Biggest match: Oklahoma City Thunder vs San Antonio Spurs
Overall: A balanced slate across two major sports...
```
