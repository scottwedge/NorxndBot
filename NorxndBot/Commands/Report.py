import discord
import os
import datetime
import asyncio
from ftplib import FTP
import json
import logging
import datetime
from discord.ext import commands
from discord.ext import tasks



class Raport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# If someone is suspicious, the user can report him
    # Report
    @commands.command(name="Report", aliases=["REPORT", "report"])
    async def Raport(self, ctx, args: discord.Member, args2="None"):
        channel = self.bot.get_channel(000000000000000000) # <- Admins / Mods channel
        await channel.send("{} Reported {} for {} !".format(ctx.author, args, args2))
        await ctx.message.delete()
        await ctx.send("Report was sent!", delete_after=3)
        LOG=("LOG TEXT")
        print(LOG)
        self.BOT_LOG.append(LOG)


def setup(bot):
    bot.add_cog(Report(bot))