import os
def getList(playerCount):
    #creates a list of games with the given player count
    listt = []
    gameDir = "/mnt/d/Code/pybot/discord_bot/games"
    for file in os.listdir(gameDir):
        gameFilePath = os.path.join(gameDir, file)
        gameFile = open(gameFilePath, "r")
        gameName = gameFile.readline().rstrip('\n')
        for line in gameFile:
            if line.rstrip('\n') == playerCount:
                listt.append(gameName)
    return listt