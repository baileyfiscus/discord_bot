import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="channel",
        description="Create a channel in the given category with the given name"
    )
    async def _channel(self, ctx: SlashContext, category: str, channel: str):
        await ctx.send("Coming soon...")
        return

    @cog_ext.cog_slash(
        name="grant",
        description="Grant the given role (if you have the necessary permissions to do so)."
    )
    async def _grant(self, ctx: SlashContext, role: str):
        print(role)
        print(discord.utils.get(ctx.guild.roles, name=role))
        #await ctx.author.add_roles(rol)


