from dotenv import load_dotenv
from sports.nba import get_todays_NBA_games
from sports.football import get_todays_football_games

load_dotenv()            

def main():
    get_todays_NBA_games() 
    get_todays_football_games()

if __name__ == "__main__":
    main()
