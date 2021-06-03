import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import random
import requests
import asyncio
import G2A
import ChessByPost
import cv2
import randomGameGenerator

class VideoGames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.g2aObj = G2A.G2A()
        self.chessDict = {}

    def get_games_list(self, players: int):
        return randomGameGenerator.get_list(players)

    @cog_ext.cog_slash(
            name = "gameslist",
            description = "Lists all squad games for the given number of players.",
            )
    async def _gameslist(self, ctx: SlashContext, players: int):
        gamesList = list(self.get_games_list(players))
        await ctx.send("Games for {} players are:\n{}".format(players, "\n".join(gamesList)))

    @cog_ext.cog_slash(
            name = "randomgame",
            description = "Chooses a random game for the given number of players.",
            )
    async def _randomgame(self, ctx: SlashContext, players: int):
        players = int(players)
        gamesList = self.get_games_list(players)
        game = "No suitable game found."
        if gamesList != []:
            game = random.choice(gamesList)
        await ctx.send("Random game for {} players:\n{}".format(players, game))

    @cog_ext.cog_slash(
            name="g2a",
            description = "Searches for the given game on G2A. Prints prices and links if found.",
            )
    async def _g2a(self, ctx: SlashContext, gamename: str):
        msg = self.g2aObj.search(gamename)
        await ctx.send(msg)

    def Chess_New_Game(self, player1, player2):
        game = ChessByPost.Controller.Controller(player1, player2)

        if not player1 in self.chessDict.keys():
            self.chessDict[player1] = {}
        self.chessDict[player1][player2] = game

        if not player2 in self.chessDict.keys():
            self.chessDict[player2] = {}
        self.chessDict[player2][player1] = game

        imgPath = "temp/board.png"
        cv2.imwrite(imgPath, game.boardImg)
        msg = "Game created for {} and {}".format(player1, player2)
        #await ctx.send(msg, file=discord.File(imgPath)) # todo
        return

    def Chess_Get_Game(self, player1, player2):
        game = None
        if player1 in self.chessDict.keys():
            if player2 in self.chessDict[player1].keys:
                game = self.chessDict[player1][player2]
        return Game

    def Chess_Move(self, game, player, startPos, endPos):
        retCode = game.Do_Move_Algebraic_Notation(player, startPos, endPos)
        imgPath = "temp/board.png"
        cv2.imwrite(imgPath, controller.boardImg)
        msg = self.Get_Chess_Message(ctx.author, retCode)
        #await ctx.send(msg, file=discord.File(imgPath))
        return

    def Chess_Forfeit(self, game, player):
        return

    def Chess_Show_Board(self, game):
        return

    def Chess_Parse_Args(self, player1, args):
        if len(args) == 0:
            return

        player2 = self.Get_Player_Name(args[0])
        game = self.Chess_Get_Game(player1, player2)

        subcommand = args[1]
        if subcommand == "move" and len(args) >= 4:
            startPos = args[2]
            endPos = args[3]
            self.Chess_Move(game, player, startPos, endPos)
        #elif subcommd == "forfeit":
        #    # Todo
        #elif subcommd == "show":
        #    # Show the current board
        #elif subcommd == "turn":
        #    # Display who's turn it is
        #elif subcommd == "":
        return

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


