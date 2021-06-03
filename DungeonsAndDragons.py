import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import random
#import requests
#import asyncio
import numpy
import pandas

allSpellsDf = pandas.read_csv("All_Spells.csv", encoding = "iso-8859-1")
allSpellsDf = allSpellsDf.fillna(0)

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
        name="spell"
    )
    async def _spell(self, ctx: SlashContext, spellname: str):
        spellInfo = "Spell not found: " + spellname
        if spellname in allSpellsDf["Spell Name"].values:
            spellEntry = allSpellsDf.loc[allSpellsDf['Spell Name'] == spellname].values.tolist()
            name, level, school, ritual, castingTime, range, area, v, s, m, component, cost, concentration, duration, effect, damageType, damageOrHeal, sourcebook, page, details, higherLevel, bard, cleric, druid, paladin, ranger, sorceror, warlock, wizard = spellEntry[0]
            spellInfo = str(name) + "\n"
            if level == 0:
                spellInfo += "Cantrip"
            else:
                spellInfo += str(level)
                if level == 1:
                    spellInfo += "st"
                elif level == 2:
                    spellInfo += "nd"
                elif level == 3:
                    spellInfo += "rd"
                else:
                    spellInfo += "th"
            spellInfo += " " + str(school) + "\n"
            spellInfo += "Casting Time: " + str(castingTime) + "\n"
            spellInfo += "Range: " + str(range) + "\n"
            if v !=0 or s != 0 or m != 0:
                spellInfo += "Componenents: "
                componentsList = []
                if v != 0:
                    componentsList.append(v)
                if s != 0:
                    componentsList.append(s)
                if m != 0:
                    componentsList.append(m)
                spellInfo += ", ".join(componentsList) + "\n"
            spellInfo += "Duration: " + str(duration) + "\n"
            classesList = []
            if bard != 0:
                classesList.append("Bard")
            if cleric != 0:
                classesList.append("Cleric")
            if druid != 0:
                classesList.append("Druid")
            if paladin != 0:
                classesList.append("Paladin")
            if ranger != 0:
                classesList.append("Ranger")
            if sorceror != 0:
                classesList.append("Sorceror")
            if warlock != 0:
                classesList.append("Warlock")
            if wizard != 0:
                classesList.append("Wizard")
            spellInfo += "Classes: " + ", ".join(classesList) + "\n"
            spellInfo += str(details) + "\n"
            if higherLevel != 0:
                spellInfo += "At Higher Levels: " + str(higherLevel) + "\n"
        await ctx.send(spellInfo)
