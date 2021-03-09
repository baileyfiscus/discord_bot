import discord
from discord.ext import commands
import random
import requests
import asyncio
import G2A
import ChessByPost
import cv2

class VideoGames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.g2aObj = G2A.G2A()
        self.chessDict = {}

    def get_games_list(self, players):
        return randomGameGenerator.getList(players)

    @commands.command(
            help = "Lists all squad games for the given number of players.",
            brief = "Lists games."
            )
    async def list_games(self, ctx, players):
        players = int(players)
        gamesList = self.get_games_list(players)
        await ctx.send("Games for {} players are: {}".format(players, gamesList))

    @commands.command(
            help = "Chooses a random game for the given number of players.",
            brief = "Chooses a random game to play."
            )
    async def random_game(self, ctx, players):
        players = int(players)
        gamesList = self.get_games_list(players)
        game = "No suitable game found."
        if gamesList != []:
            game = random.choice(gamesList)
        await ctx.send("Random game for {} players: {}".format(players, game))

    @commands.command(
            help = "Searches for the given game on G2A. Prints prices and links if found.",
            brief = "Search for game on G2A."
            )
    async def g2a(self, ctx, *gameName):
        name = " ".join(gameName)
        msg = self.g2aObj.search(name)
        await ctx.send(msg)

    @commands.command(
            help = "todo",
            brief = "todo"
            )
    async def chess(self, ctx, *args):
        msg = ""
        imgPath = ""

        if ctx.author in self.chessDict:
            controller = self.chessDict[ctx.author]
            msg = controller.Do_Move_Algebraic_Notation(ctx.author, args[0], args[1])
            imgPath = "temp/board.png"
            cv2.imwrite(imgPath, controller.Get_Board_Image(controller.board))
        else:
            otherPlayer = args
            controller = ChessByPost.Controller.Controller(ctx.author, otherPlayer)
            self.chessDict[ctx.author] = controller
            self.chessDict[otherPlayer] = controller
            msg = "Game created for {} and {}".format(ctx.author, otherPlayer)
            imgPath = "temp/board.png"
            cv2.imwrite(imgPath, controller.Get_Board_Image(controller.board))

        if imgPath != "":
            await ctx.send(msg, file=discord.File(imgPath))
        else:
            await ctx.send(msg)


