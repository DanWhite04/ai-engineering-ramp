# AI Engineering Ramp

Self-directed applied AI engineering study, working toward a junior role in the LLM / API engineering space.

Each numbered folder is a milestone — a standalone project with its own working code, dependencies, and notes. The progression is deliberate: fundamentals → real-world integrations → the LLM stack. I write the code; this repo is the public record of the ramp.

## Background

Bachelor of Information Technology, Macquarie University (Sydney, 2026). Strong Java foundation; this repo is my structured ramp into the Python-first AI engineering stack.

## Milestones

| # | Folder | Focus | Status |
|---|--------|-------|--------|
| 01 | [`01-warmup/`](01-warmup/) | Python fundamentals — loops, OOP/inheritance, dicts, file I/O, JSON | Done |
| 02 | [`02-sports-dashboard/`](02-sports-dashboard/) | Multi-API integration — live NBA games + 5 European football leagues, with auth headers, env-loaded secrets, timezone-aware date handling, and graceful empty-result behaviour | Done |
| 03 | `03-pydantic/` | Type hints, pydantic models, validated structures | Next |
| 04 | `04-claude-hello/` | First Anthropic SDK calls; streaming; structured outputs | — |
| 05 | `05-fastapi/` | HTTP service wrapper around LLM endpoints | — |
| 06 | `06-capstone/` | End-to-end LLM-powered tool combining real APIs with Claude | — |

## Tech stack

- **Python 3.14** with [`uv`](https://docs.astral.sh/uv/) for project/environment management
- **Milestone 2**: `requests`, `python-dotenv`, `zoneinfo` / `tzdata`
- **Later milestones**: `pydantic`, `fastapi`, the official `anthropic` Python SDK

## Running a milestone

Each folder is a standalone `uv` project:

```bash
cd 02-sports-dashboard
uv run python main.py
```

Milestones that hit external APIs need a `.env` file with the relevant keys — see each milestone's local notes for required variables. `.env` is gitignored; nothing sensitive is committed.
