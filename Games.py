import random

class Game:
  def __init__(self, name, playersList, buyLinks):
    self.name = name
    self.playersList = playersList
    self.buyLinks = buyLinks

  def GetPrices(self):
    if self.buyLinks == []:
      return "No price links listed"
    prices = []
    for site in buyLinks:
      price = 1 # todo find price
      prices.append(price)
    # For g2a, any games's webpage appears to have a div of class "product-page-v2-price__price" which has the game's price
    return prices


class Games:
  def __init__(self):
    self.gamesList = self.UpdateGamesList()

  def UpdateGamesList(self):
    gamesList = []
    # todo parse spreadsheet for data
    return gamesList

  def GetRandomGame(self, players):
    suitableGames = []
    for game in self.gamesList:
      if players in game.playersList:
        suitableGames.append(game.name)

    if suitableGames != []:
      game = random.choice(self.gamesList)
      return game
    else:
      return []
