import requests

r = requests.get('http://api.football-data.org/v1/competitions/467/fixtures')

data = r.json()

match = 0
matchData = data["fixtures"][match]
awayTeam = matchData["awayTeamName"]
homeTeam = matchData["homeTeamName"]
goalsHome = matchData["result"]["goalsHomeTeam"]
goalsAway = matchData["result"]["goalsAwayTeam"]

print(homeTeam, goalsHome, '-', goalsAway, awayTeam)