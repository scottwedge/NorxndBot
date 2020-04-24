import discord
import os
import datetime
import asyncio
from ftplib import FTP
import json
import logging
from discord.ext import commands
from discord.ext import tasks




class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # Help
        @commands.command(name="Help", aliases=["HELP"])
        async def help_command(self, ctx):
            info = discord.Embed(title="NorxndBot Help", description="Information", color=0xefbf01)
            info.add_field(name="?Help", value="Show help", inline=False)
            info.add_field(name="?Rules", value="Show server Rules", inline=True)
            info.add_field(name="?Roles", value="See server roles and its meaning", inline=True)
            info.add_field(name="?CovidInfo", value="See info about SARS-COV-2 and COVID-19", inline=False)
            info.add_field(name="?VipLinks", value="Official Vip servers list", inline=False)
            await ctx.send(embed=info, delete_after=60)

            config = discord.Embed(description="Configuration", color=0xefbf01)
            config.add_field(name="?FeLevel 25", value="Type your FE2 Level and get rank", inline=False)
            config.add_field(name="?GameNewsletter", value="Add or remove yourself from FE2 Newestller", inline=True)
            config.add_field(name="?Bruhhg", value="Add or remove Bruhhg role", inline=True)
            config.add_field(name="?Rage", value="Add or remove Rage role", inline=True)
            config.add_field(name="?Girl",
                             value="Add or remove The Girl Gang role (Please. if you are not girl, DONT use that!)",
                             inline=True)
            config.add_field(name="?NorxndBotTest", value="Add or remove yourself from NorxndBot Improve Program",
                             inline=True)
            await ctx.send(embed=config, delete_after=60)

            req = discord.Embed(description="Requests", color=0xefbf01)
            req.add_field(name='?RoleReq "Dev"', value="Request for role", inline=False)
            req.add_field(name='?IdeaReq ', value='Idea for server / NorxndBot improving', inline=True)
            req.add_field(name='?ServReq "Flood Escape 2" "LINK"', value="Request for add Vip server to list",
                          inline=True)
            await ctx.send(embed=req, delete_after=60)

            other = discord.Embed(description="Rest", color=0xefbf01)
            other.add_field(name='?Commit "Flood Escape 2" "(Vip server link)"',
                            value="Tell others you playing a game! (Use vip server link, or LAN or IP or something else!)",
                            inline=True)
            other.add_field(name="?AdminHelp", value="Only for Staff Team and above!", inline=True)
            await ctx.send(embed=other, delete_after=60)

            embed = discord.Embed(title="NorxndBot {}".format(self.bot.Version),
                                  url="https://github.com/norxnd/norxndbot", description="By NORXND Unname",
                                  color=0xefbf01)
            embed.add_field(name="Fallow @NORXND_Unname on Twitter", value="patreon.com/norxnd", inline=False)
            embed.set_footer(
                text="Thanks to Piotr Baja, realpython.com, discord.py discord server community and Heroku")
            await ctx.send(embed=embed, delete_after=60)

            await ctx.message.delete()
            LOG = ("{} used Help command with arguments:".format(ctx.author))
            print(LOG)
            self.bot.BOT_LOG.append(LOG)

        # AdminHelp
        @commands.command(name="AdminHelp", aliases=["ADMINHELP", "adminhelp"])
        @commands.has_any_role("Staff Team")
        async def AdminHelp(self, ctx):
            embed = discord.Embed(title="NorxndBot Admin Help", description="?Help - Normal Help", color=0xfa8700)
            embed.add_field(name='?Announcement "Information"', value="Send Announcement", inline=False)
            embed.add_field(name='?Warn @User "Reason"', value="Warn user", inline=True)
            embed.add_field(name='?Purge 5', value="Delete number of messages", inline=True)
            embed.add_field(name='?Alert @User "Alert"', value="Send user alert via DM", inline=True)
            embed.add_field(name='?Send CHANNEL ID "Text"', value="Send messages to channel", inline=True)
            embed.add_field(name='?SendDM @User "Text"', value="Send DM to user", inline=True)
            embed.set_footer(
                text="?Log 0 - See bot log(0 - for all logs or number).ONLY FOR ADMINISTRATOR AND ABOVE!!!")
            await ctx.send(embed=embed, delete_after=30)
            await ctx.message.delete()
            LOG = ("{} used AdminHelp command with arguments: at {}".format(ctx.author, datetime.datetime.utcnow()))
            print(LOG)
            self.bot.BOT_LOG.append(LOG)


# If you are starting adventure with NorxndBot, dont remove this command. Go to Roles first! If you know how to use pre-installed commands you can write own Help command!




def setup(bot):
    bot.add_cog(Help(bot))