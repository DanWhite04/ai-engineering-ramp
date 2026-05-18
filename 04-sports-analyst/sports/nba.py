"""NBA data source — fetches today's games from balldontlie.io.

Returns a list of dicts in the unified format shared with sports.football,
so the analyst layer can treat games from any sport uniformly.
"""

import os
from datetime import datetime
from zoneinfo import ZoneInfo

import requests


NBA_API_URL = "https://api.balldontlie.io/v1/games"


def _normalise_status(api_status: str) -> str:
    """Map balldontlie status strings onto the unified status values."""
    if "Qtr" in api_status or "Halftime" in api_status:
        return "in_progress"
    elif api_status == "Final":
        return "finished"
    else:
        return "scheduled"


def get_todays_NBA_games() -> list[dict]:
    """Return today's NBA games as a list of unified-format dicts.

    Uses US Eastern time for "today" because the NBA API indexes games by
    the US-local date the game is scheduled on.
    """
    api_key = os.getenv("NBA_API_KEY")
    today = datetime.now(ZoneInfo("America/New_York")).date().isoformat()

    response = requests.get(
        NBA_API_URL,
        headers={"Authorization": api_key},
        params={"dates[]": today},
    )
    data = response.json()

    games = []
    for game in data["data"]:
        games.append(
            {
                "sport": "Basketball",
                "competition": "NBA",
                "home_team": game["home_team"]["full_name"],
                "away_team": game["visitor_team"]["full_name"],
                "home_score": game["home_team_score"],
                "away_score": game["visitor_team_score"],
                "status": _normalise_status(game["status"]),
            }
        )
    return games
