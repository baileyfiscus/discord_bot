import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import random
import requests
import asyncio
import myToken
import AccessGoogleSheet
import VideoGames
import DungeonsAndDragons
import numpy
import pandas
import guilds

command_prefix='$'
intents = discord.Intents.all()
bot = commands.Bot(command_prefix, intents=intents)
slash = SlashCommand(bot, sync_commands=True)

bot.add_cog(VideoGames.VideoGames(bot))
bot.add_cog(DungeonsAndDragons.DungeonsAndDragons(bot))

@slash.slash(name="ping", guild_ids=guilds.guild_ids)
async def _pint(ctx):
    await ctx.send("pong")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')
    # Create banned users array
    # Create gameslist objects list

bot.run(myToken.bot_token)
