import discord
from discord.ext import commands
import re
from core import checks
from core.models import PermissionLevel

class SlowMode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def slowmode(self, ctx, time, channel: discord.TextChannel = None):
        """💬 Set a slowmode to a channel
        It is not possible to set a slowmode longer than 6 hours
        """
if seconds >= 0:
        if ctx.channel.slowmode_delay == seconds:
            embed=discord.Embed(
                title="",
                description=f":x: Slowmode is already set up to `{seconds}` second(s) in {ctx.channel.mention} :x:",
                color=0xff0000
            )
            await ctx.send(embed=embed)
        else:
            await ctx.channel.edit(slowmode_delay=seconds)
            embed=discord.Embed(
                title="",
                description=f":white_check_mark: Slowmode is set up to `{seconds}` second(s) :white_check_mark:",
                color=discord.Color.random()
            )
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(SlowMode(bot))
