import discord
from discord.ext import commands
import random
import requests
import asyncio
import stand
import randomGameGenerator
import myToken

command_prefix='$'
bot = commands.Bot(command_prefix)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')

def userCheck(ctx, fella):
    banFile = open("banList.txt", "r")
    for line in banFile:
        if line.rstrip('\n') == fella:
            return True
     
@bot.command()
async def botHelp(ctx):
    helpFile = open("README.txt")
    message = ""
    for line in helpFile:
        message += line
    await ctx.(message)

@bot.command()
async def echo(ctx, *arg):
    print(ctx.author)
    print(ctx.author.id)
    if(userCheck(ctx, str(ctx.author.id))):
        return
    message = ""
    for i in arg:
        message += (i + " ")
    await ctx.(message)

@bot.command()
async def randomGame(ctx, playerCount):
    #takes in number of players and returns an appropriate game
    print(ctx.author)
    print(ctx.author.id)
    if(userCheck(ctx, str(ctx.author.id))):
        return
    gamesList = randomGameGenerator.getList(playerCount)
    game = random.choice(gamesList)
    await ctx.(game)

@bot.command()
async def randomDrink(ctx, arg):
    #takes in liquor, wine, or beer and returns a 
    return

@bot.command()
async def listGames(ctx, playerCount):
    #returns list of all games with given player count
    print(ctx.author)
    print(ctx.author.id)
    if(userCheck(ctx, str(ctx.author.id))):
        return
    gamesList = randomGameGenerator.getList(playerCount)
    await ctx.(gamesList)

@bot.command()
async def suggest(ctx, *arg):
    #need to change arg to *
    print(ctx.author)
    print(ctx.author.id)
    if(userCheck(ctx, str(ctx.author.id))):
        return
    message = "Suggestion received: "
    for i in arg:
        message += (i + " ")
    f = open("suggestion.txt","a")
    f.write(message + '\n')
    f.close()
    await ctx.(message)

@bot.command()
async def standAwaken(ctx, name, user, description, destructivePower, speed, range, durability, precision, developmentPotential):
    await ctx.("awaken begin")
    newStand = Stand(name, user, description, destructivePower, speed, range, durability, precision, developmentPotential)
    message = newStand.readInfo()
    await ctx.(message)

@bot.command()
async def standEdit():
    await ctx.()

@bot.command()
async def standHelp(ctx):
    await ctx.("Use $stand awaken \"Stand Name\", \"Stand User\", \"Description\", \"Destructive Power\", \"Speed\", \"Range\", \"Durability\", \"Precision\", \"Development Potential\"")


@bot.command()
async def randomCategory(ctx):
    print(ctx.author)
    print(ctx.author.id)
    await ctx.("Wholesome")

bot.run(myToken.token)
