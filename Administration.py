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
        fellaRole = discord.utils.get(ctx.guild.roles, name="Fellas")
        if fellaRole not in ctx.author.roles:
            await ctx.send("You do not have permission to be granted roles by me.")
            return

        if not role.startswith("<@&"):
            await ctx.send("Please @ the role you wish to have granted.")
            return

        rolename = discord.utils.get(ctx.guild.roles, id=int(role[3:-1]))

        if rolename == discord.utils.get(ctx.guild.roles, name="Admin"):
            await ctx.send("Reeee gimme admin reeee.")
            return

        if rolename == None:
            await ctx.send("Could not find that role.")
            return

        try:
            await ctx.author.add_roles(rolename)
            await ctx.send("Granted {}.".format(rolename))
        except:
            await ctx.send("I cannot grant {}.".format(rolename))
        return


