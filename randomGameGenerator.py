import os

def getList(playerCount):
    #creates a list of games with the given player count
    gamesList = []
    gameDir = "/home/pi/discord_bot/games"
    print(playerCount)
    for file in os.listdir(gameDir):
        gameFilePath = os.path.join(gameDir, file)
        gameFile = open(gameFilePath, "r")
        gameName = gameFile.readline().rstrip('\n')
        for line in gameFile:
            number_of_players = line.rstrip('\n')
            if number_of_players  == str(playerCount):
                gamesList.append(gameName)
    return gamesList
