import os
import requests
from dotenv import load_dotenv
from datetime import datetime , timezone
from zoneinfo import ZoneInfo


def get_todays_football_games():
        competitions = ["PL", "PD", "BL1", "SA", "FL1"]
        API_KEY = os.getenv("FOOTBALL_API_KEY")
        today = datetime.now(timezone.utc).date().isoformat()
        total_matches_found = 0;
        for comp in competitions:
            url = f"https://api.football-data.org/v4/competitions/{comp}/matches"
            
            params ={
                
                
                "dateFrom": today,
                "dateTo" : today,
            }

            headers = {
                "X-Auth-Token" : API_KEY
            }

            response = requests.get(url, headers=headers, params=params) 
            data = response.json()
            matches = data["matches"]

            for game in matches:
                 total_matches_found += 1

            if total_matches_found == 0:
                 print("No football matches scheduled today.")

            for game in data["matches"]:
                home_name = game["homeTeam"]["name"]
                visitor_name = game["awayTeam"]["name"]
                home_score = game["score"]["fullTime"]["home"] if game["score"]["fullTime"]["home"] is not None else "TBD"
                visitor_score = game["score"]["fullTime"]["away"] if game["score"]["fullTime"]["away"] is not None else "TBD"
                competition = game["competition"]["name"]

                print(f"{competition} - {home_name} {home_score} - {visitor_score} {visitor_name}")