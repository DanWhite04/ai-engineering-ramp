"""AI Sports Analyst — entry point.

Fetches today's NBA games and major-league football matches from public APIs,
sends the combined list to Claude for a structured analysis, and prints a
human-readable summary.
"""

from dotenv import load_dotenv

load_dotenv(override=True)

from sports.nba import get_todays_NBA_games
from sports.football import get_todays_football_games
from analyst import analyse_today


def main() -> None:
    """Orchestrate: fetch data, run analysis, present results."""
    nba_games = get_todays_NBA_games()
    football_games = get_todays_football_games()
    all_games = nba_games + football_games

    if not all_games:
        print("No games scheduled today.")
        return

    analysis = analyse_today(all_games)

    print(f"=== {analysis.headline} ===\n")
    for game in analysis.games:
        print(f"  {game.matchup} ({game.competition})")
        print(f"    {game.storyline}\n")
    print(f"Biggest match: {analysis.biggest_match}")
    print(f"Overall: {analysis.overall_review}")


if __name__ == "__main__":
    main()
