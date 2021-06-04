import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import random
import numpy
import pandas
import difflib
import math

allSpellsDf = pandas.read_csv("spells.csv", delimiter="\t", encoding = "utf-8", index_col=False)
allSpellNames = allSpellsDf['Name'].tolist()

class DungeonsAndDragons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="roll",
        description="Rolls a die with the given number of sides"
    )
    async def _roll(self, ctx: SlashContext, sides: int):
        message = "{} is an invalid number to roll.".format(sides)
        if sides > 0:
            val = random.randint(1, sides)
            message = "Rolling {}-sided die... rolled {}".format(sides, val)
        await ctx.send(message)

    @cog_ext.cog_slash(
        name="spell",
        description="Provides information about the given D&D 5E spell"
    )
    async def _spell(self, ctx: SlashContext, spellname: str):
        closestMatch = difflib.get_close_matches(spellname, allSpellNames, n=1)
        if (len(closestMatch) == 0):
            await ctx.send("Spell not found: " + spellname)
            return
        spellname = closestMatch[0]
        spellIndex = numpy.where(allSpellsDf['Name'] == spellname)[0]
        spellEntry = allSpellsDf.iloc[spellIndex]

        todo = "todo"
        embed=discord.Embed(color=0xffff00, title=spellname)

        embed.add_field(name="Level", value=spellEntry['Level'].values[0], inline=True)
        embed.add_field(name="School", value=spellEntry['School'].values[0], inline=True)

        embed.add_field(name="Ritual", value=spellEntry['Ritual'].values[0], inline=True)

        embed.add_field(name="Casting Time", value=spellEntry['Casting Time'].values[0], inline=True)
        embed.add_field(name="Range", value=spellEntry['Range'].values[0], inline=True)

        components = ""
        if spellEntry['Verbal'].values[0] == True:
            components += "V "
        if spellEntry['Somatic'].values[0] == True:
            components += "S "
        if spellEntry['Material'].values[0] == True:
            components += "M ({})".format(spellEntry['Materials'].values[0])
        embed.add_field(name="Components", value=components, inline=False)

        embed.add_field(name="Concentration", value=spellEntry['Concentration'].values[0], inline=True)
        embed.add_field(name="Duration", value=spellEntry['Duration'].values[0], inline=True)

        embed.add_field(name="Classes", value=spellEntry['Classes'].values[0], inline=False)

        MAX_FIELD_VALUE_LENGTH = 1024
        description = spellEntry['Description'].values[0].replace("\\n", '\n')
        firstChunk = True
        startIndex = 0
        endIndex = MAX_FIELD_VALUE_LENGTH
        while startIndex < len(description):
            fieldName = "​" # no-width character to hide field name
            if firstChunk:
                fieldName = "Description"
                firstChunk = False

            endIndex = startIndex + MAX_FIELD_VALUE_LENGTH
            print("StartIndex = {}".format(startIndex))
            if (len(description) > endIndex) and ("\n" in description[startIndex:endIndex]):
                print("Splitting at newline")
                # split description by last newline in this chunk
                endIndex = description.rfind('\n', startIndex, endIndex)

            print("EndIndex = {}".format(endIndex))
            descriptionChunk = description[startIndex:endIndex]
            startIndex = endIndex
            
            embed.add_field(name=fieldName, value=descriptionChunk, inline=False)
        await ctx.send(embed=embed)

