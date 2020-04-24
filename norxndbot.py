Version = "0.1.0.1" # <- For version

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

bot = commands.Bot(command_prefix='PREFIX')

bot.Version = Version # <- You will need that if you use Version
bot.BOT_LOG = [] # <- For Bot Logs
# bot.ftp = FTP('FTP SERVER') <- For FTP / Storage Service

# You can use this loop to have a few activities!
""""
@tasks.loop(seconds=True)
async def status_change_loop():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="GAME NAME"))
    await asyncio.sleep(15) <- 15 is the time when activities change
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="MOVIE NAME"))
    await asyncio.sleep(15)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="SONG NAME"))
    await asyncio.sleep(15)
"""

# If you use FTP storage, you can use it to update you bot log from a file at start
""""
def UpdateLog():
    localfile = open("LOG FILE NAME", 'wb')
    bot.ftp.retrbinary('RETR ' + "LOG FILE NAME", localfile.write, 1024)
    localfile.close()
    bot.BOT_LOG.append(json.load(open('LOG FILE NAME')))
"""

# And this to upload file
""""
@tasks.loop(seconds=120) <- 120 is the time when the file will be uploaded
async def UpdateLog_loop():
    bot.ftp.storbinary('STOR ' + "LOG FILE NAME", open("LOG FILE NAME", 'rb'))
"""

@bot.event # Everything you put in this function will start when the bot starts
async def on_ready():
    # status_change_loop.start() <- Use this if you use function from 22-29 lines in this file!
    print("MESSAGE IN TERMINAL WHEN BOT RUNS")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="NAME")) # You can change type to playing, watching and listening!
    # bot.ftp.login(user='FTP USERNAME', passwd='FTP PASSWORD') <- Use only when you use FTP
    # UpdateLog() <- Use this if you use function from 34-38 lines in this file!
    bot.BOT_LOG.append("MESSAGE TO LOGS WHEN BOT RUNS")
    # UpdateLog_loop.start() <- Use this if you use function from 43-45 lines in this file!




core = ['NorxndBot.Commands.Info.Help','NorxndBot.Commands.Info.Rules','NorxndBot.Commands.Info.Roles','NorxndBot.Commands.Admin','NorxndBot.Commands.CovidInfo', 'NorxndBot.Events.BadWordsDetector', 'NorxndBot.Commands.Report', 'NorxndBot.Events.BotLog'] # List of commands etc. that pre-installed!

extensions = [] # You can add you own commands and functions in another file by adding it to this list!
"""
Example:
extension = ['Folder.Folder.File', 'Folder.Folder.File2', 'Folder.Folder2.File']
"""



for coreex in core: # Loader for commands etc. that pre-installed.
    bot.load_extension(coreex)

for extension in extensions: # Loader for your own commands and extensions!
    bot.load_extension(extension)




bot.run('TOKEN')



