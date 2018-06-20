twoPlayerGames = ["Borderlands", "Borderlands 2", "Cards Against Humanity Online", "CS:GO", "Darwin Project", "Civ 5", "Civ 6", "Deceit", "Fortnite", "Gary's Mod", "Killing Floor", "Killing Floor 2", "Left 4 Dead 2", "Payday 2", "Rocket Car Game", "Sir You Are Being Hunted", "Smite", "Star Wars: Battlefront 2", "Team Fortress 2", "Town of Salem", "Warhammer Vermintide"]
threePlayerGames = ["Borderlands", "Borderlands 2", "Cards Against Humanity Online", "CS:GO", "Darwin Project", "Civ 5", "Civ 6", "Deceit", "Fortnite", "Gary's Mod", "Killing Floor", "Killing Floor 2", "Left 4 Dead 2", "Payday 2", "Rocket Car Game", "Sir You Are Being Hunted", "Smite", "Star Wars: Battlefront 2", "Team Fortress 2", "Town of Salem", "Warhammer Vermintide"]
fourPlayerGames = ["Borderlands", "Borderlands 2", "Cards Against Humanity Online", "CS:GO", "Darwin Project", "Civ 5", "Civ 6", "Deceit", "Fortnite", "Gary's Mod", "Killing Floor", "Killing Floor 2", "Left 4 Dead 2", "Payday 2", "Rocket Car Game", "Sir You Are Being Hunted", "Smite", "Star Wars: Battlefront 2", "Team Fortress 2", "Town of Salem", "Warhammer Vermintide"]
fivePlayerGames = ["Cards Against Humanity Online", "CS:GO", "Darwin Project", "Civ 5", "Civ 6", "Deceit", "Gary's Mod", "Killing Floor", "Killing Floor 2", "Smite", "Star Wars: Battlefront 2", "Team Fortress 2", "Town of Salem"]
sixPlayerGames = ["Cards Against Humanity Online", "Darwin Project", "Civ 5", "Civ 6", "Deceit", "Gary's Mod", "Killing Floor", "Killing Floor 2", "Rocket Car Game", "Star Wars: Battlefront 2", "Town of Salem"]
sevenPlayerGames = ["Cards Against Humanity Online", "Civ 5", "Civ 6", "Gary's Mod", "Star Wars: Battlefront 2", "Town of Salem"]
eightPlayerGames = ["Cards Against Humanity Online", "Civ 5", "Civ 6", "Gary's Mod", "Rocket Car Game", "Star Wars: Battlefront 2", "Town of Salem"]
ninePlayerGames = ["Cards Against Humanity Online", "Civ 5", "Civ 6", "Gary's Mod", "Star Wars: Battlefront 2", "Town of Salem"]
tenPlayerGames = ["Cards Against Humanity Online", "Civ 5", "Civ 6", "Gary's Mod", "Smite", "Star Wars: Battlefront 2", "Town of Salem"]
mmoPlayerGames = ["Cards Against Humanity Online", "Civ 5", "Civ 6", "Gary's Mod", "Star Wars: Battlefront 2", "Town of Salem"]

gameDict = {'2' : twoPlayerGames, '3' : threePlayerGames, '4' : fourPlayerGames, '5' : fivePlayerGames, '6' : sixPlayerGames, '7' : sevenPlayerGames, '8' : eightPlayerGames, '9' : ninePlayerGames, '10' : tenPlayerGames, 'more' : mmoPlayerGames}

def getList(playerCount):
    return random.choice(gameDict[str(playerCount)])