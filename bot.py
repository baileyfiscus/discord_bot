import discord
from discord.ext import commands
import random
import requests
import asyncio
import stand
import randomGameGenerator
import myToken
import AccessGoogleSheet

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
  if message.author == bot.user:
    return
  if Ban.InBanList(message.author):
    return

  print(str(message.author) + " - " + str(message.content))

  if message.content.startswith(command_prefix):
    response = Process_Command(message.content[len(command_prefix):])
    await message.channel.send(response)
  elif message.author.bot:
    # Messages was written by another bot
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
      

def Process_Command(command):
  if command.startswith("randomGame"):
    players = int(command[len("randomGame"):])
    gamesList = randomGameGenerator.getList(players)
    print(str(players))
    print(gamesList)
    if gamesList != []:
      game = random.choice(gamesList)
      return game
    else:
      return "No games found for " + str(players) + " players."
  return

bot.run(myToken.bot_token)
