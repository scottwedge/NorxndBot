import discord
import os
import datetime
import asyncio
from ftplib import FTP
import json
import logging
from discord.ext import commands
from discord.ext import tasks


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# Send an announcement to channel
    # Announcement
    @commands.command(name="Announcement", aliases=["ANNOUNCEMENT", "announcement"])
    @commands.has_any_role("ADMIN / MODERATOR ROLE NAME") # Thanks to this line, only users with this role can use the command !
    async def ann(self, ctx, args):
        channel = self.bot.get_channel(563004560113926154)
        await channel.send(f"ANNOUNCEMENT TEXT LIKE @everyone New announcement + {args}") # <- Args is text that you type into a command like ?Announcement "Text".
        await ctx.message.delete()
        LOG=("MESSAGE TO LOG")
        print(LOG)
        self.bot.BOT_LOG.append(LOG)


# Deletes number of messages
    # Purge
    @commands.command(name="Purge", aliases=["PURGE", "purge"])
    @commands.has_any_role("ADMIN / MODERATOR ROLE NAME")
    async def clean(self, ctx, limit: int): # Limit is how many messages you want to delete
        limit = limit + 1
        await ctx.channel.purge(limit=limit) # Delete messages
        await ctx.send("Deleted {} messages!".format(limit-1), delete_after=3) # This is optional. You can use f"TEXT {Variable}" or "TEXT".format(Variable)
        LOG=("MESSAGE TO LOG")
        print(LOG)
        self.bot.BOT_LOG.append(LOG)


# NorxndBot warn systen
    # Warn
    @commands.command(name="Warn", aliases=["WARN", "warn"])
    @commands.has_any_role("ADMIN / MODERATOR ROLE NAME")
    async def Warn(self, ctx, args1: discord.Member, args2="no reason"):
        Member = args1
        WarnOne = ctx.guild.get_role(000000000000000000) # In this 0 enter 1st Warning role ID
        WarnTwo = ctx.guild.get_role(000000000000000000) # In this 0 enter 2nd Warning role ID
        WarnTree = ctx.guild.get_role(000000000000000000) # In this 0 enter 3rd Warning role ID
        WarnFour = ctx.guild.get_role(000000000000000000) # In this 0 enter 4th Warning role ID
        Action = "warned" # Optional
        for roles in Member.roles: # Check all roles that member have
            if roles != WarnOne: # If checks is Member's role isn't 1st Warning
                await Member.add_roles(WarnOne) # Add 1st Warning role
            if roles == WarnOne: # If checks is Member's role is 1st Warning
                await Member.add_roles(WarnTwo) # Add 2nd Warning role
            if roles == WarnTwo: # If checks is Member's role is 2nd Warning
                await Member.add_roles(WarnTree) # Add 3rd Warning role
                Action = "kicked" # Optional
                await self.bot.kick(Member) # Kick member out of the server
            if roles == WarnTree:
                await Member.add_roles(WarnFour) # Add 4th Warning role
                Action = "banned" # Optional
                await ctx.guild.ban(Member, reason=args2) # Ban Member

        channel = await Member.create_dm() # Remember sending messages to specific channels? This is for sending DMS, and you use it the same as await channel.send()
        await channel.send("MESSAGE TO WARNED / KIECKED / BANNED PERSON") # You can use ctx.author for tell user who warned him and args2 that tell user reason of his warning. You can use action to tell user if he was warned, kicked or banned
        await ctx.message.delete()
        await ctx.send("Warned {}".format(args1), delete_after=3) # Optional. ctx.send() send a message to channel where trigger command was sent
        LOG=("MESSAGE TO LOGS") # You can use datetime.datetime.now() in a format to add time to your logs. You can use datetime.datetime.utcnow() to add time in UTC
        print(LOG)
        self.bot.BOT_LOG.append(LOG)


# Send alert to User
    # Alert
    @commands.command(name="Alert", aliases=["ALERT", "alert"])
    @commands.has_any_role("ADMIN / MODERATOR ROLE NAME")
    async def Alert(self, ctx, args1: discord.Member, args2="This must be mistake"): # self,ctx,args1 etc. Is command arguments. You MUST have ctx. You must have self if command isn't in main bot file.
        Member = args1
        channel = await Member.create_dm()
        await channel.send(f"MESSAGE LIKE You get alert: {args2}") # args2 is Your alert ?Alert "Text"
        await ctx.message.delete()
        await ctx.send("Alert sent", delete_after=3) # Optional
        LOG=("TEXT TO LOG") # For log I recommend f"{ctx.author} used COMMAND NAME command with arguments: {ARGUMENT 1} and {ARGUMENT 2} and {ARGUMENT 3} (If you only have ctx and self you don't must write with arguments..., if you got only one add on argument you don't have to type and) at {datetime.datetime.utcnow()}"
        print(LOG)
        self.bot.BOT_LOG.append(LOG)


# Send custom message to specyfic channel
    # Send
    @commands.command(name="Send", aliases=["SEND", "send"])
    @commands.has_any_role("ADMIN / MODERATOR ROLE NAME")
    async def Send(self, ctx, channel: discord.TextChannel, text):
        await channel.send(text)
        await ctx.message.delete()
        LOG=("LOG TEXT")
        print(LOG)
        self.bot.BOT_LOG.append(LOG)

# Send custom DM to user
    # SendDM
    @commands.command(name="SendDM", aliases=["SENDDM", "senddm"])
    @commands.has_any_role("ADMIN / MODERATOR ROLE NAME")
    async def SendDM(self, ctx, Member: discord.Member, text):
        channel = await Member.create_dm()
        await channel.send(text)
        await ctx.message.delete()
        await ctx.send("DM sent to {}".format(Member), delete_after=3)
        LOG=("LOG TEXT")
        print(LOG)
        self.bot.BOT_LOG.append(LOG)

# Show bot log (Recommended only for Owner and Admins!)
    @commands.command(name="Log", aliases=["LOG", "log"])
    @commands.has_any_role("ADMIN / MODERATOR ROLE NAME")
    async def LOG(self, ctx, entry: int = None):
        await ctx.message.delete()
        if entry == None:
            await ctx.send("Please select entry!")
        elif entry == 0:
            for entries in self.bot.BOT_LOG:
                await ctx.send(entries)
        else:
            await ctx.send(self.bot.BOT_LOG[entry])
        LOG = ("LOG TEXT")
        print(LOG)
        self.bot.BOT_LOG.append(LOG)


def setup(bot):
    bot.add_cog(Admin(bot))





