import discord
import os
import datetime
import asyncio
from ftplib import FTP
import json
import logging
from discord.ext import commands
from discord.ext import tasks

class BadWordsDetector(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    bot_bannedwords = ["BAD WORDS", "MORE BAD WORDS"] # Use BADWORD, badword and Badword !

    def log(self, msg, state="POST"):
        f = open('./chat.log', 'a+')
        f.write(str(datetime.datetime.now()))
        f.write('\t' + state)
        f.write('\t' + str(msg.id))
        f.write('\t' + str(msg.author.id))
        f.write('\t' + '"' + msg.author.name + '"')
        f.write('\t' + str(msg.channel.id))
        f.write('\t' + '"' + msg.channel.name + '"')
        f.write('\t' + '"' + msg.content + '"')
        try:
            f.write('\t' + '"' + str(msg.embeds[0]) + '"')
        except:
            f.write('\t' + 'NO_EMBEDS')
        try:
            f.write('\t' + '"' + str(msg.attachments[0]) + '"')
        except:
            f.write('\t' + 'NO_ATTACHMENTS')

        f.write('\n')
        f.close()

    @commands.Cog.listener()
    async def on_message(self, ctx):
        BadWordsDetector.log(self, ctx)
        for b in BadWordsDetector.bot_bannedwords:
            if b in ctx.content:
                await ctx.delete() # Delets message with bad word!
                channel = self.bot.get_channel(ctx.channel.id)
                await channel.send("MESSAGE IN CHANNEL") # Like f"Dont use bad words {ctx.author}" <- ctx.author is author of message!
                LOG = ("MESSAGE TO LOGS")
                print(LOG)
                self.bot.BOT_LOG.append(LOG)


def setup(bot):
    bot.add_cog(BadWordsDetector(bot))
