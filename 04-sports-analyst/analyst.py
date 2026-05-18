"""Claude-powered analyst that turns a list of game dicts into a structured DayAnalysis."""

import json

import anthropic
from dotenv import load_dotenv

from models import DayAnalysis


load_dotenv(override=True)
client = anthropic.Anthropic()

MODEL = "claude-haiku-4-5"
TOOL_NAME = "report_day_analysis"
SYSTEM_PROMPT = (
    "You are a well-versed, punchy, observant sports analyst. "
    "Given today's fixtures and results, provide a concise daily analysis with personality."
)


def analyse_today(games: list[dict]) -> DayAnalysis:
    """Send today's games to Claude and return a validated DayAnalysis.

    Uses tool-use with the DayAnalysis JSON schema so Claude is forced to
    return structured output matching the pydantic model exactly.
    """
    games_json = json.dumps(games, indent=2)

    response = client.messages.create(
        model=MODEL,
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        tools=[
            {
                "name": TOOL_NAME,
                "description": "Report the day's sports analysis as a structured object.",
                "input_schema": DayAnalysis.model_json_schema(),
            }
        ],
        tool_choice={"type": "tool", "name": TOOL_NAME},
        messages=[
            {
                "role": "user",
                "content": f"Today's games:\n\n{games_json}\n\nAnalyse the day.",
            }
        ],
    )

    tool_block = next(b for b in response.content if b.type == "tool_use")
    return DayAnalysis(**tool_block.input)
