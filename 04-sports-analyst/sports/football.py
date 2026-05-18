"""Football data source — fetches today's matches across major European leagues.

Returns a list of dicts in the unified format shared with sports.nba, so the
analyst layer can treat games from any sport uniformly.
"""

import os
from datetime import datetime, timezone

import requests


COMPETITIONS = ["PL", "PD", "BL1", "SA", "FL1"]  # Premier League, La Liga, Bundesliga, Serie A, Ligue 1
COMPETITION_URL = "https://api.football-data.org/v4/competitions/{code}/matches"


def _normalise_status(api_status: str) -> str:
    """Map football-data.org status strings onto the unified status values."""
    if api_status in ("LIVE", "IN_PLAY", "PAUSED"):
        return "in_progress"
    elif api_status == "FINISHED":
        return "finished"
    else:
        return "scheduled"


def get_todays_football_games() -> list[dict]:
    """Return today's football matches across the configured competitions.

    Uses UTC for "today" because football-data.org indexes matches by UTC date.
    """
    api_key = os.getenv("FOOTBALL_API_KEY")
    today = datetime.now(timezone.utc).date().isoformat()

    games = []
    for code in COMPETITIONS:
        response = requests.get(
            COMPETITION_URL.format(code=code),
            headers={"X-Auth-Token": api_key},
            params={"dateFrom": today, "dateTo": today},
        )
        data = response.json()

        for match in data["matches"]:
            games.append(
                {
                    "sport": "Football",
                    "competition": match["competition"]["name"],
                    "home_team": match["homeTeam"]["name"],
                    "away_team": match["awayTeam"]["name"],
                    "home_score": match["score"]["fullTime"]["home"],
                    "away_score": match["score"]["fullTime"]["away"],
                    "status": _normalise_status(match["status"]),
                }
            )
    return games
