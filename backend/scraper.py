import requests
import _json
def NFLScores():
    request = requests.get("https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events")
    game = request.json()
    gameList = []
    for i in game['items']:
        gameList.append( i['$ref'])    
    for Jindex, i in enumerate(gameList):
        gameList[Jindex]= requests.get(i).json()
    #only 1 competition
    gameStats = []
    for i in range(len(gameList)):
        gameStats.append(gameList[i]['competitions'][0]['competitors'])
    teamScore = []
    for Iindex in range(len(gameStats)):
        gameSum = [{"team": 'null', "score": 0},{"team": 'null', "score": 0}]
        for Jindex, i in enumerate(gameStats[Iindex]):
            score = requests.get(i['score']['$ref']).json()
            gameSum[Jindex]['score'] = score['value']
            team = requests.get(i['team']['$ref']).json()
            gameSum[Jindex]['team'] = team['displayName']#use shortDisplayName for their nick name
        teamScore.append(gameSum)
    return teamScore