Version = "0.1.5.0P" # Version

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

bot.Version = Version
bot.BOT_LOG = []
# bot.ftp = FTP('FTP SERVER') For FTP database
bot.StarCodes = {}


@tasks.loop(seconds=True) # Status change loop
async def status_change_loop():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="?Help for commands, help and info!"), status=discord.Status.online)
    await asyncio.sleep(15)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"NorxndBot {Version} by Norxnd Unname"), status=discord.Status.online)
    await asyncio.sleep(15)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Fallow @NORXND_Unname on Twitter & Support on patron.com/norxnd"), status=discord.Status.online)
    await asyncio.sleep(15)

# Database


"""
For update files on bot start - Use FTP

def Update():
    # BotLog
    localfile = open("BotLog.json", 'wb')
    bot.ftp.retrbinary('RETR ' + "BotLog.json", localfile.write, 1024)
    localfile.close()
    bot.BOT_LOG.append(json.load(open('BotLog.json')))
    # StarCodes
    localfile = open("StarCodes.json", 'wb')
    bot.ftp.retrbinary('RETR ' + "StarCodes.json", localfile.write, 1024)
    localfile.close()
    bot.StarCodes = json.load(open('StarCodes.json'))
"""

"""
Send files to FTP server

@tasks.loop(seconds=120)
async def Sync():
        # BotLog
        j = json.dumps(bot.BOT_LOG)
        f = open('BotLog.json', 'w')
        f.write(j)
        f.close()
        bot.ftp.storbinary('STOR ' + "BotLog.json", open("BotLog.json", 'rb'))
"""


# End of database


@bot.event
async def on_ready():
    status_change_loop.start()
    print("TEXT WHEN BOT START")

    #bot.ftp.login(user='FTP USERNAME', passwd='FTP PASSWORD')
    #Update()
    bot.BOT_LOG.append("{}".format(Version))
    #Sync.start()


"""
This command will be trigger when error occurs in command! - BETA

@bot.event
async def on_command_error(ctx, error):
    try:
        status_change_loop.stop()
        await bot.change_presence(status=discord.Status.idle)
        await ctx.send(f"{ctx.author} An {error} error occurred while executing the command! ",delete_after=10)
        await ctx.message.delete()
        await asyncio.sleep(10)
        status_change_loop.start()
        LOG = f"ON COMMAND ERROR - Error: {error} Message: {ctx.message}"
        print(LOG)
        bot.BOT_LOG.append(LOG)
        raise error
    except RuntimeError:
        print("Task isnt complate, but it was lunched again!")
"""







core = ['NorxndBot.Commands.Info.Help','NorxndBot.Commands.Info.Rules','NorxndBot.Commands.Info.Roles','NorxndBot.Commands.Admin','NorxndBot.Commands.CovidInfo', 'NorxndBot.Events.BadWordsDetector', 'NorxndBot.Commands.Report', 'NorxndBot.Events.Welcome', 'NorxndBot.Commands.Info.Channels'] # Pre installed extensions

extensions = [] # Your extensions eg. Files with functions / code / Commands.

"""
extensions = ['file', 'folder.file', 'folder.folder.file', 'folder.folder.secound file', 'secound folder.folder.file]
"""



for coreex in core: # Loader for core extensions
    bot.load_extension(coreex)

for extension in extensions: # Loader for your extensions
    bot.load_extension(extension)


"""
Often when the bot starts, there is a RuntimeError error: Event Loop is closed but but everything works normally. 
Ignore it. Therefore, do not worry about errors I created a simple function that just 
write a message instead of giving the whole Traceback (Error).
"""
try:
    bot.run('TOKEN') # From Discord developer portal
except RuntimeError:
    print("There was RuntimeError: Event Loop is closed. error again!")
