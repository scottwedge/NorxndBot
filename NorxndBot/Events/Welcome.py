import discord
import os
import datetime
import asyncio
from ftplib import FTP
import json
import logging
from discord.ext import commands
from discord.ext import tasks

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, Member):
        Role = Member.guild.get_role(000000000000000000) # Optional, for auto role
        await Member.add_roles(Role)
        LOG = f"{Member} joined server" # Message to logs
        print(LOG)
        self.bot.BOT_LOG.append(LOG)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """
        How it works:
        There is a message in a channel, if someone gives reaction ✅  (:green_check_mark:) to this message, he will gain role!
        """
        Guild = self.bot.get_guild(000000000000000000) # Your server ID
        Member = Guild.get_member(payload.user_id)
        Role = Member.guild.get_role(00000000000000000) # Role that will be given
        DR = Member.guild.get_role(000000000000000000) # Role that person must have like New.
        if payload.message_id == 000000000000000000: # ID of message where reaction must be given
            if payload.emoji.name == "✅": # ✅ you can change it to another emoji, search in discord.py docs: https://discordpy.readthedocs.io/en/latest/
                await Member.add_roles(Role)
                await Member.remove_roles(DR)
                LOG = f"{Member} entered server"
                print(LOG)
                self.bot.BOT_LOG.append(LOG)



def setup(bot):
    bot.add_cog(Welcome(bot))
