import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from asyncio import sleep
import sys
import random
import os

class social():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief='posts reis twitch link', description='posts reis twitch link')
    async def twitch(self, ctx):
        await self.bot.say("lol my gay owners twitch is https://www.twitch.tv/reitrace")

    @commands.command(pass_context=True, brief='posts reis steam link', description='posts reis steam link')
    async def steam(self, ctx):
        await self.bot.say('heres a gay steam account i found: https://www.steamcommunity.com/id/last2live')

    @commands.command(pass_context=True, brief='posts reis deviantart link', description='posts reis deviantart link')
    async def deviantart(self, ctx):
        await self.bot.say('heres a trash deviantart account: https://www.deviantart.com/reitrace')

    @commands.command(pass_context=True, brief='posts reis instagram link', description='posts reis instagram link')
    async def instagram(self, ctx):
        await self.bot.say('lol follow my insta: https://www.instagram.com/reitrace')


def setup(bot):
    bot.add_cog(social(bot))
