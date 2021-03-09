import discord
from discord.ext import commands
import random
import requests
import asyncio
import myToken
import AccessGoogleSheet
import VideoGames
import DungeonsAndDragons
import numpy
import pandas

command_prefix='$'
intents = discord.Intents.all()
bot = commands.Bot(command_prefix, intents=intents)


bot.add_cog(VideoGames.VideoGames(bot))
bot.add_cog(DungeonsAndDragons.DungeonsAndDragons(bot))

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')
    # Create banned users array
    # Create gameslist objects list

bot.run(myToken.bot_token)
