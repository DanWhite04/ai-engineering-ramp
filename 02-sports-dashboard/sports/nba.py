import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from zoneinfo import ZoneInfo


def get_todays_NBA_games():
        API_KEY = os.getenv("NBA_API_KEY")
        today = datetime.now(ZoneInfo("America/New_York")).date().isoformat()
        url = "https://api.balldontlie.io/v1/games"

        params ={
             
             "dates[]": today
        }

        headers = {
            "Authorization" : API_KEY
        }
        response = requests.get(url, headers=headers, params=params) 

       

        data = response.json()

        if not data["data"]:
            print("No NBA games scheduled today.")
            return

        for game in data["data"]:
            home_name = game["home_team"]["full_name"]
            visitor_name = game["visitor_team"]["full_name"]
            home_score = game["home_team_score"] if game["home_team_score"] is not None else "TBD"
            visitor_score = game["visitor_team_score"] if game["visitor_team_score"] is not None else "TBD"

            print(f"{home_name} {home_score} - {visitor_score} {visitor_name}")