"""
This is just a layout you can copy paste and edit as you like when adding a new cog.
"""
from discord.ext import commands
from discord.ext.commands import Cog


class ExampleCog(Cog, name="Example"):
    """This is where you describe what the functionality of this cog is."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="test")
    async def command_name(self, ctx):
        """Brief description of the command functionality"""
        return await ctx.send("This seems to be working alright....")


def setup(bot):
    bot.add_cog(ExampleCog(bot))
