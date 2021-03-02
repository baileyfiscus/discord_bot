import discord
from discord.ext import commands
import random
import requests
import asyncio
import urllib.parse
import logging

from bs4 import BeautifulSoup

class G2A:
    # TODO there's got to be some function for building URLs in urllib.parse

    def __init__(self):
        self.baseUrl = 'https://www.g2a.com/{}?{}'
        return

    def search(self, name):
        return self.formatter(self.scrape(name))

    def get_url(self, subpage, **kwargs):
        return self.baseUrl.format(subpage, urllib.parse.urlencode(kwargs))

    def scrape_card(self, card):
        price = card.find("span", class_="Card__price-cost").text
        title_obj = next(card.find("h3", class_="Card__title").children)
        url = "https://www.g2a.com" + title_obj.get("href")
        title = title_obj.text
        return title, url, price

    def scrape(self, search_query, num_results=3):
        "Returns a list of query results from G2A."
        url = self.get_url("search", query=search_query)
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
        soup = BeautifulSoup(resp.content, features="html.parser")
        itr = soup.find_all("li", class_="products-grid__item")
        card_items = list(itr)[:num_results]
        result = []
        for card in card_items:
            try:
                title, url, price = self.scrape_card(card)
                result.append({"title": title, "url": url, "price": price})
            except (AttributeError, TypeError) as e:
                logger.debug("Parsing error in Games.py:scrape: {}", str(e))
                print("Parsing error in Games.py:scrape: {}", str(e)) # DEBUG
        resp.close()
        return result

    def formatter(self, info):
        msg = "I found these results on G2A:\n\n"

        for item in info:
            print(item)
            try:
                msg += "*[{title}]({url})*\nPrice: ${price}\n\n".format(**item)
            except KeyError as e:
                logger.debug("Games.py:formatter: ", str(e))
        print(msg)

        return msg

