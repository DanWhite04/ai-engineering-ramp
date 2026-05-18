# AI Sports Analyst

Fetches today's NBA games and major European football matches from public APIs, sends the combined list to Claude via the official Anthropic SDK, and prints a structured, validated daily analysis.

## What it demonstrates

- **Multi-source data integration.** Two sports APIs with different authentication schemes (a Bearer-style header on one, a custom `X-Auth-Token` on the other), unified into a single internal schema before they reach the analyst layer.
- **Structured LLM output.** Pydantic models define the contract for the response. Anthropic tool-use forces Claude to produce schema-compliant JSON, removing the need for fragile string parsing.
- **Clean separation of concerns.** `sports/` handles I/O, `analyst.py` handles the AI call, `models.py` defines the schema, and `main.py` orchestrates the pipeline.
- **Timezone-aware date handling.** NBA dates are queried in US Eastern time and football in UTC, matching what each upstream API indexes by.

## Project layout

```
04-sports-analyst/
├── main.py            # entry point; orchestrates fetch, analyse, print
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

You'll need three environment variables in `.env`:

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
