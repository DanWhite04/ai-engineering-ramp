"""Pydantic models defining the contract for Claude's daily sports analysis."""

from pydantic import BaseModel


class GameAnalysis(BaseModel):
    """A short analysis of a single fixture or result."""

    matchup: str
    sport: str
    competition: str
    storyline: str


class DayAnalysis(BaseModel):
    """The full structured verdict for a day's sport across all sources."""

    headline: str
    games: list[GameAnalysis]
    biggest_match: str
    overall_review: str
