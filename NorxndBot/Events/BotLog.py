import discord
import os
import datetime
import asyncio
from ftplib import FTP
import json
import logging
from discord.ext import commands
from discord.ext import tasks

class BotLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.BotLog_SaveLoop.start()

# Saves logs to file
"""""    
    @tasks.loop(seconds=120)
    async def BotLog_SaveLoop(self):

        j = json.dumps(self.bot.BOT_LOG)

        f = open('LOG FILE NAME', 'w')
        f.write(j)
        f.close()
"""

def setup(bot):
    bot.add_cog(BotLog(bot))

