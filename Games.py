import random
import urllib.parse
import logging

import requests

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

# TODO there's got to be some function for building URLs in urllib.parse
G2A_BASE = 'https://www.g2a.com/{}?{}'

def g2a_url(subpage, **kwargs):
  return G2A_BASE.format(subpage, urllib.parse.urlencode(kwargs))

def scrape_g2a_card(card):
  price = card.find("span", class_="Card__price-cost").text
  title_obj = next(card.find("h3", class_="Card__title").children)
  url = title_obj.get("href")
  title = title_obj.text
  return title, url, price

def scrape_g2a(search_query, num_results=3):
  "Returns a list of query results from G2A."
  url = g2a_url("search", query=search_query)
  headers = {
    # TODO these are just settings I got from using the web inspector in
    # Firefox on windows 10. Other settings may work.
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
  }
  resp = requests.get(url, headers=headers)
  soup = BeautifulSoup(resp.content)
  itr = soup.find_all("li", class_="products-grid__item")
  card_items = list(itr)[:num_results]
  result = []
  for card in card_items:
    try:
        title, url, price = scrape_g2a_card(card)
        result.append({"title": title, "url": url, "price": price})
    except (AttributeError, TypeError) as e:
      logger.debug("Parsing error in Games.py:scrape_g2a: {}", str(e))
 l     # print("Parsing error in Games.py:scrape_g2a: {}", str(e)) # DEBUG
  resp.close()
  return result

def g2a_formatter(g2a_info):
  msg = "I found these results on G2A:\n\n"

  for item in g2a_info:
    try:
      msg += "*[{title}]({url})*\nPrice: ${price}\n\n".format(**item)
    except KeyError as e:
      logger.debug("Games.py:g2a_formatter: ", str(e))

  return msg

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
      # For g2a, any games's webpage appears to have a div of class
      # "product-page-v2-price__price" which has the game's price
    return prices

class Games:
  def __init__(self):
    self.gamesList = self.UpdateGamesList()

  def UpdateGamesList(self):
    gamesList = []
    # TODO parse spreadsheet for data
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
