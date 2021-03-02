import discord
from discord.ext import commands
import random
import requests
import asyncio
import G2A

class VideoGames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.g2aObj = G2A.G2A()

    def get_games_list(self, players):
        return randomGameGenerator.getList(players)

    @commands.command()
    async def list_games(self, ctx, players):
        players = int(players)
        gamesList = self.get_games_list(players)
        await ctx.send("Games for {} players are: {}".format(players, gamesList))

    @commands.command()
    async def random_game(self, ctx, players):
        players = int(players)
        gamesList = self.get_games_list(players)
        game = "No suitable game found."
        if gamesList != []:
            game = random.choice(gamesList)
        await ctx.send("Random game for {} players: {}".format(players, game))

    @commands.command()
    async def g2a(self, ctx, *args):
        name = " ".join(args)
        print(name)
        msg = self.g2aObj.search(name)
        print(msg)
        await ctx.send(msg)

