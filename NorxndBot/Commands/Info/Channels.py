import discord
import os
import datetime
import asyncio
from ftplib import FTP
import json
import logging
from discord.ext import commands
from discord.ext import tasks




class Channels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Channels", aliases=["CHANNELS", "channels"]) # Basic Information command
    async def Channels(self, ctx):
        # Text Example
        """""
        Help = ("Text \n"
        "You can write in next line by enter \n"
        "Dont forget about "" !")
        await ctx.send(Help) - Send Message
        """
        # Embed Example
        """
        embed=discord.Embed(title="TITLE", url="httpsTITLE URL", description="DESCRIPTION", color=HEX COLOR)
        embed.set_author(name="AUTHOR NAME", url="AUTHOR LINK", icon_url="AUTHOR ICON")
        embed.set_thumbnail(url="THUMBNAIL URL")
        embed.add_field(name="FIELD NAME", value="FIELD VALUE", inline=False / True)
        embed.add_field(name="2 FIELD NAME", value="2 FIELD VALUE", inline=False / True)
        embed.set_footer(text="FOOTER TEXT")
        await ctx.send(embed=embed)
        """

        await ctx.message.delete()
        LOG = ("{} used Channels command with arguments: at {}".format(ctx.author, datetime.datetime.utcnow()))
        print(LOG)
        self.bot.BOT_LOG.append(LOG)

def setup(bot):
    bot.add_cog(Channels(bot))