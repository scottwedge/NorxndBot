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

    bot_bannedwords = ["fuck", "idiot", "kid", "bitch", "shit", "Fuck", "Idiot", "Kid", "Bitch", "Shit", "FUCK",
                       "IDIOT", "KID", "BITCH", "SHIT", 'skit'] # Your bad words, use bad word BAD WORD and Bad word !

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
                await ctx.delete() # Delete message with a bad word!
                channel = self.bot.get_channel(ctx.channel.id)
                await channel.send("Don't use bad words {}!".format(ctx.author.name)) # Like f"Don't use bad words {ctx.author}" <- ctx.author is author of message!
                LOG = ("MESSAGE TO LOG") # <- You can use "TEXT {}".format(Variable) or f"TEXT {Variable}"
                print(LOG)
                self.bot.BOT_LOG.append(LOG)
        # Mute system
        Member = ctx.author
        Role = ctx.guild.get_role(000000000000000000) # <- Your mute role
        for roles in Member.roles:
            if roles == Role: # If member have Mute role, it deletes his every message that he send!
                await ctx.delete()


def setup(bot):
    bot.add_cog(BadWordsDetector(bot))
