from re import I
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import difflib
import numpy
import pandas
import pathlib

SUGGESTED_CHANNELS_FILENAME = "suggested_channels.csv"

class Suggestion():
    def __init__(self, category, channel, approvals = ['','',''], denials = ['','','']):
        self.category = category
        self.channel = channel
        self.approvals = approvals
        self.denials = denials

    def Approve(self, approver):
        self.approvals.append(approver)

    def Deny(self, denier):
        self.denials.append(denier)

class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.suggestedChannels = {}
        if not pathlib.Path(SUGGESTED_CHANNELS_FILENAME).is_file():
            self.WriteSuggestedChannels()
        self.ReadSuggestedChannels()

    def WriteSuggestedChannels(self):
        with open(SUGGESTED_CHANNELS_FILENAME, 'w+') as f:
            f.write("Category\tChannel\tApprove 1\tApprove 2\tApprove 3\tDeny 1\tDeny 2\tDeny 3\n")
            for suggestion in self.suggestedChannels.values():
                while len(suggestion.approvals) < 3:
                    suggestion.approvals.append('')

                while len(suggestion.denials) < 3:
                    suggestion.denials.append('')

                line = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
                    suggestion.category,
                    suggestion.channel,
                    suggestion.approvals[0],
                    suggestion.approvals[1],
                    suggestion.approvals[2],
                    suggestion.denials[0],
                    suggestion.denials[1],
                    suggestion.denials[2])
                f.write(line)
        return

    def ReadSuggestedChannels(self):
        df = pandas.read_csv(SUGGESTED_CHANNELS_FILENAME, delimiter='\t', encoding = "utf-8", index_col=False)
        df = df.replace(numpy.nan, '', regex=True)
        for index, row in df.iterrows():
            searchName = "/".join([row['Category'].lower(), row['Channel'].lower()])
            self.suggestedChannels[searchName] = Suggestion(
                row['Category'],
                row['Channel'],
                [row['Approve 1'], row['Approve 2'], row['Approve 3']],
                [row['Deny 1'], row['Deny 2'], row['Deny 3']])

    @cog_ext.cog_subcommand(
        base="channel",
        name="suggest",
        description="Suggest a channel to have created."
        )
    async def _channel_suggest(self, ctx: SlashContext, category: str, channel: str):
        # Check if category exists
        categoryNames = [x.name for x in ctx.guild.categories]
        if not category.lower() in map(str.lower, categoryNames):
            await ctx.send("Could not find category: {}".format(category))
            return
        category = categoryNames[list(map(str.lower, categoryNames)).index(category.lower())]

        # Check if channel already exists
        channelNames = [x.name for x in ctx.guild.channels]
        if channel.lower() in map(str.lower, channelNames):
            await ctx.send("A channel named {} already exists.".format(channel))
            return
        
        # Check if channel has already been suggested
        searchName = '/'.join([category.lower(),channel.lower()])
        if searchName in self.suggestedChannels.keys():
            await ctx.send("A channel named {} has already been suggested.\n\nPlease use the `channel` `approve` command.".format(channel))
            return

        self.suggestedChannels[searchName] = Suggestion(category, channel, [ctx.author.id])
        self.WriteSuggestedChannels()
        await ctx.send("Suggested channel `{}` in category `{}`.\n\nAwaiting two more approvals.".format(channel, category))
        return

    @cog_ext.cog_subcommand(
        base="channel",
        name="list",
        description="List all suggested channels."
        )
    async def _channel_list(self, ctx: SlashContext):
        msg = "Current suggested channels:\n\nCATEGORY : CHANNEL\n"
        channelsList = []
        for suggestion in self.suggestedChannels.values():
            channelsList.append("{} : {}".format(suggestion.category, suggestion.channel))
        msg += "\n".join(channelsList)
        await ctx.send(msg)

    @cog_ext.cog_subcommand(
        base="channel",
        name="approve",
        description="Suggest a channel to have created."
        )
    async def _channel_approve(self, ctx: SlashContext, category: str, channel: str):
        self.ReadSuggestedChannels()

        # Check if category and channel pair already exist
        searchName = "/".join([category.lower(), channel.lower()])
        if not searchName in self.suggestedChannels.keys():
            await ctx.send("No such channel has been suggested.\n\nPlease use the `channel` `suggest` command.")
            return
        
        suggestion = self.suggestedChannels[searchName]

        # todo see if user has permission to create channels, then just skip approvals

        if ctx.author.id in suggestion.approvals:
            await ctx.send("You have already approved this channel.")
            return

        if suggestion.approvals[0] == '':
            # todo this shouldn't happen
            await ctx.send("Error, no first approver.")
            return
        elif suggestion.approvals[1] == '':
            suggestion.approvals[1] = ctx.author.id
            await ctx.send("Approved channel `{}` in category `{}`.\n\nAwaiting one more approval.".format(channel, category))
        else:
            category = discord.utils.get(ctx.guild.categories, name=suggestion.category)
            await ctx.guild.create_text_channel(suggestion.channel, category=category)
            del self.suggestedChannels[searchName]
            await ctx.send("Approved channel `{}` in category `{}`.\n\nCreated channel.".format(channel, category))

        self.WriteSuggestedChannels()
        return

    @cog_ext.cog_subcommand(
        base="channel",
        name="deny",
        description="Deny a suggested channel."
        )
    async def _channel_deny(self, ctx: SlashContext, category: str, channel: str):
        self.ReadSuggestedChannels()

        # Check if category and channel pair already exist
        searchName = "/".join([category.lower(), channel.lower()])
        if not searchName in self.suggestedChannels.keys():
            await ctx.send("No such channel has been suggested.\n\nPlease use the `channel` `suggest` command.")
            return
        
        suggestion = self.suggestedChannels[searchName]

        # todo see if user has permission to create channels, then just skip denials

        if ctx.author.id in suggestion.denials:
            await ctx.send("You have already denied this channel.")
            return

        if suggestion.denials[0] == '':
            suggestion.denials[0] = ctx.author.id
            await ctx.send("Denied channel `{}` in category `{}`.\n\nAwaiting two more denial.".format(channel, category))
        elif suggestion.denials[1] == '':
            suggestion.denials[1] = ctx.author.id
            await ctx.send("Denied channel `{}` in category `{}`.\n\nAwaiting one more denial.".format(channel, category))
        else:
            del self.suggestedChannels[searchName]
            await ctx.send("Denied channel `{}` in category `{}`.\n\nRemoved channel suggestion.".format(channel, category))

        self.WriteSuggestedChannels()
        return

    @cog_ext.cog_subcommand(
        base="role",
        name="check",
        description="Check the permissions of one of your roles."
        )
    async def _role_check(self, ctx: SlashContext, category: str, channel: str):
        await ctx.send("Suggested channel {} in category {}".format(channel, category))
        return

    @cog_ext.cog_subcommand(
        base="role",
        name="list",
        description="List all possible roles that you can add."
        )
    async def _role_list(self, ctx: SlashContext, category: str, channel: str):
        return

    @cog_ext.cog_subcommand(
        base="role",
        name="add",
        description="Suggest a channel to have created."
        )
    async def _role_add(self, ctx: SlashContext, role: str):
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

    @cog_ext.cog_subcommand(
        base="role",
        name="remove",
        description="Remove one of your roles."
        )
    async def _role_remove(self, ctx: SlashContext, role: str):
        return
