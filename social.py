from discord.ext import commands

class social():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief='posts reis twitch link')
    async def twitch(self, ctx):
        await self.bot.say("lol my gay owners twitch is https://www.twitch.tv/reitrace")

    @commands.command(pass_context=True, brief='posts reis steam link')
    async def steam(self, ctx):
        await self.bot.say('heres a gay steam account i found: https://www.steamcommunity.com/id/last2live')

    @commands.command(pass_context=True, brief='posts reis deviantart link')
    async def deviantart(self, ctx):
        await self.bot.say('heres a trash deviantart account: https://www.deviantart.com/reitrace')

    @commands.command(pass_context=True, brief='posts reis instagram link')
    async def instagram(self, ctx):
        await self.bot.say('lol follow my insta: https://www.instagram.com/reitrace')

    @commands.command(pass_context=True, brief='post reis website link')
    async def website(self, ctx):
        await self.bot.say('heres some trash website my trash owner never finished working on, https://www.reitrace.ga')
        await self.bot.say('at least it has https, thank you certbot')

def setup(bot):
    bot.add_cog(social(bot))
