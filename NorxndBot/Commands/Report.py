from norxndbot import *



class Report(commands.Cog):
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
        self.bot.BOT_LOG.append(LOG)


def setup(bot):
    bot.add_cog(Report(bot))