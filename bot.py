import discord
from discord.ext import commands
import random
import requests
import asyncio
import stand
import randomGameGenerator
import myToken
import AccessGoogleSheet
import Games

command_prefix='$'
bot = commands.Bot(command_prefix)

@bot.event
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  print('-----')
  # Create banned users array
  # Create gameslist objects list

@bot.event
async def on_message(message):
  # Ignore our own messages. Important!
  if message.author == bot.user:
    return

  # Don't accept commands from banned users.
  if Ban.InBanList(message.author):
    return

  # Handle a command.
  if message.content.startswith(command_prefix):
    response = process_command(message.content[len(command_prefix):])
    await message.channel.send(response)

  # Handle messages from other bots.
  elif message.author.bot:
    for embed in message.embeds:
      descriptionList = str(embed.description).splitlines()
      print(descriptionList)
      if (len(descriptionList) == 7):
        if (descriptionList[2].startswith("Length")):
          songName, songLink = descriptionList[0].split('https')
          print(songName)
          print(songLink)
          songName = songName[1:-1]
          songLink= 'https' + songLink[:-1]
          songRequestor = descriptionList[4][len("Requested by:") + 3:]
          AccessGoogleSheet.AddSongEntry(songName, songLink, songRequestor)

def process_command(command):
  # TODO Write a grammar to tokenize the commands instead of just splitting
  cmd = command.split(" ")

  if cmd[0] == "randomGame":
    players = int(command[len("randomGame"):])
    # TODO store in memory / memoize with mtime?
    gamesList = randomGameGenerator.get_list(players)
    print(str(players))
    print(gamesList)
    if gamesList != []:
      game = random.choice(gamesList)
      return game

    else:
      return "No games found for " + str(players) + " players."

  elif cmd[0] == "g2a":
    if len(cmd) > 2:
      cmd[2] = int(cmd[2])

    g2a_info = Games.scrape_g2a(*cmd[1:])
    return g2a_formatter(g2a_info)

bot.run(myToken.bot_token)
