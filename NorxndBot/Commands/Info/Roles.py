import discord
import os
import datetime
import asyncio
from ftplib import FTP
import json
import logging
from discord.ext import commands
from discord.ext import tasks



class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# Basic information command!
    @commands.command(name="Roles", aliases=["ROLES", "roles"])
    async def roles(self, ctx):
        # Text Example
        """""
        Help = ("Text \n"
        "You can write in next line by typing \n"
        "Dont forget about "" !")

        await ctx.send(Help)
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
        # You can use await ctx.send(Help, embed=embed) !
        # In ctx.send you can use ", delete_after=SECONDS" to delete bot message after a few seconds!

        await ctx.message.delete()
        LOG = ("MESSAGE TO LOG")
        print(LOG)
        self.bot.BOT_LOG.append(LOG)



def setup(bot):
    bot.add_cog(Roles(bot))