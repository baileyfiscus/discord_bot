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

    def Get_Chess_Message(self, playerName, retCode):
        msg = ""
        if retCode == ChessByPost.Controller.ReturnCode.UNKNOWN_ERROR:
            msg = "An unknown error has occurred.".format()
        elif retCode == ChessByPost.Controller.ReturnCode.PLAYER_NOT_FOUND:
            msg = "Player not found: {}.".format(playerName)
        elif retCode == ChessByPost.Controller.ReturnCode.NOT_PLAYERS_TURN:
            msg = "It is not {}'s turn.".format(playerName)
        elif retCode == ChessByPost.Controller.ReturnCode.INVALID_COORD:
            msg = "Move failed: inavlid coordinate.".format()
        elif retCode == ChessByPost.Controller.ReturnCode.NO_PIECE_AT_COORD:
            msg = "Move failed: no piece at coordinate.".format()
        elif retCode == ChessByPost.Controller.ReturnCode.INVALID_MOVE :
            msg = "Move failed: that is not a valid move.".format()
        elif retCode == ChessByPost.Controller.ReturnCode.INVALID_MOVE_KING_IN_CHECK :
            msg = "Move failed: king will still be in check.".format()
        elif retCode == ChessByPost.Controller.ReturnCode.SUCCESSFUL_MOVE :
            msg = "Successful move.".format()
        elif retCode == ChessByPost.Controller.ReturnCode.SUCCESSFUL_MOVE_KING_IN_CHECK :
            msg = "Successful move: king is now in check!".format()
        elif retCode == ChessByPost.Controller.ReturnCode.SUCCESSFUL_MOVE_CHECKMATE :
            msg = "Successful move: checkmate!".format()
            otherPlayerName = self.chessDict[playerName]
            self.chessDict.pop(playerName)
            self.chessDict.pop(otherPlayerName)
            # controller should get cleaned up by the garbage collector
        elif retCode == ChessByPost.Controller.ReturnCode.GAMEOVER:
            msg = "Error: game is already over.".format()
        else:
            msg = "Something went wrong: not a valid return code."
        return msg

    @commands.command(
            help = "todo",
            brief = "todo"
            )
    async def chess(self, ctx, *args):
        retCode = ChessByPost.Controller.ReturnCode.UNKNOWN_ERROR
        imgPath = ""

        if ctx.author in self.chessDict:
            controller = self.chessDict[ctx.author][0]
            retCode = controller.Do_Move_Algebraic_Notation(ctx.author, args[0], args[1])
            imgPath = "temp/board.png"
            cv2.imwrite(imgPath, controller.boardImg)
        else:
            otherPlayer = args[0]
            print(otherPlayer)
            if not otherPlayer.startswith("<@!"):
                msg = "Error: you must @ the other player."
                await ctx.send(msg)
                return
            otherPlayer = otherPlayer[3:-1]
            print(otherPlayer)
            isInChannel = False
            for member in ctx.channel.members:
                if str(member.id) == str(otherPlayer):
                    otherPlayer = member
                    isInChannel = True
                    break
            if not isInChannel:
                msg = "Error: the other person must be in this channel."
                await ctx.send(msg)
                return
            if otherPlayer == ctx.author:
                msg = "Error: you cannot play against yourself. It's just sad."
                await ctx.send(msg)
                return
            controller = ChessByPost.Controller.Controller(ctx.author, otherPlayer)
            self.chessDict[ctx.author] = (controller, otherPlayer)
            self.chessDict[otherPlayer] = (controller, ctx.author)
            imgPath = "temp/board.png"
            cv2.imwrite(imgPath, controller.boardImg)
            msg = "Game created for {} and {}".format(ctx.author, otherPlayer)
            await ctx.send(msg, file=discord.File(imgPath))
            return

        msg = self.Get_Chess_Message(ctx.author, retCode)
        if imgPath != "":
            await ctx.send(msg, file=discord.File(imgPath))
        else:
            await ctx.send(msg)


