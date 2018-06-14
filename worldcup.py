import requests

def get_data(url):
    ''' Returns World Cup 2018 data in JSON format'''
    r = requests.get(url)
    return r.json()

def get_results(data, game):
    gameData = data["fixtures"][game]

    results = {}
    status = gameData["status"]  
    results["status"] = status  

    homeTeam = gameData["homeTeamName"]
    results["homeTeam"] = homeTeam

    goalsHome = gameData["result"]["goalsHomeTeam"]
    results["goalsHome"] = goalsHome

    awayTeam = gameData["awayTeamName"]
    results["awayTeam"] = awayTeam

    goalsAway = gameData["result"]["goalsAwayTeam"]
    results["goalsAway"] = goalsAway

    return results 


def main():
    url = 'http://api.football-data.org/v1/competitions/467/fixtures'
    data = get_data(url)
    n_games = data["count"]

    for game in range(n_games):
        results = get_results(data, game)
        if results["status"] != "SCHEDULED":
            if None in (results["goalsHome"], results["goalsAway"]):
                print(results["homeTeam"], "- Game Not Played -", results["awayTeam"])
            else:
                print(results["homeTeam"], results["goalsHome"], '-', results["goalsAway"], results["awayTeam"])
    
    

if __name__ == '__main__':
    main()