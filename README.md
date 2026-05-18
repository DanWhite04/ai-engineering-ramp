# AI Engineering Ramp

A self-directed study working toward a junior role in applied LLM and AI engineering.

Each numbered folder is a standalone project with its own working code, dependencies, and notes. The progression is deliberate: fundamentals first, then real-world integrations, then the LLM stack itself. I write the code; this repo is the public record of the progress as I go.

## Background

Bachelor of Information Technology, Macquarie University (Sydney, 2026). My foundation is in Java, and this repo is my structured ramp into the Python-first AI engineering stack.

## Milestones

| # | Folder | Focus | Status |
|---|--------|-------|--------|
| 01 | [`01-warmup/`](01-warmup/) | Python fundamentals: loops, OOP and inheritance, dicts, file I/O, JSON | Done |
| 02 | [`02-sports-dashboard/`](02-sports-dashboard/) | Multi-API integration. Live NBA games and five European football leagues with auth headers, env-loaded secrets, timezone-aware dates, and graceful empty-result handling | Done |
| 03 | [`03-claude-hello/`](03-claude-hello/) | Anthropic SDK basics: pydantic models, tool-use for structured output, system prompts, multi-turn conversation, streaming | Done |
| 04 | [`04-sports-analyst/`](04-sports-analyst/) | Capstone. End-to-end AI sports analyst that combines the data layer from M2 with Claude tool-use from M3 to produce a validated daily analysis | Done |
| 05 | `05-rag/` | RAG project: embeddings, vector database, semantic retrieval, citations. The headline portfolio piece | Next |
| 06 | `06-fastapi/` | Optional. HTTP service wrapping the RAG system as a REST API | Planned |

## Tech stack

- **Python 3.14** with [`uv`](https://docs.astral.sh/uv/) for project and environment management
- **Milestone 2**: `requests`, `python-dotenv`, `zoneinfo` and `tzdata`
- **Milestone 3 onward**: `pydantic`, the official `anthropic` Python SDK
- **Later milestones**: a vector database (likely Chroma), `fastapi`

## Running a milestone

Each folder is a standalone `uv` project:

```bash
cd 04-sports-analyst
uv run python main.py
```

Milestones that hit external APIs need a `.env` file with the relevant keys. See each milestone's local README for the required variables. The `.env` is gitignored, so nothing sensitive is committed.
