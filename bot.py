import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from asyncio import sleep
import sys
import random
import os

startup_extensions = ["fun", "social"]

f = open('token.txt', 'r')
token = f.read()
f.seek(0)
f.close()

f = open('owner.txt', 'r')
ownerid = f.read()
f.seek(0)
f.close()

f = open('lastgame.txt', 'r')
argtxt = f.read()
f.seek(0)
f.close()

f = open('prefix.txt', 'r')
p = f.read()
f.seek(0)
f.close()

client = commands.Bot(command_prefix=p)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(game=discord.Game(name=argtxt))

@client.command(pass_context=True, brief='forces reibot to respond pong.', description='forces reibot to respond pong. used for testing the bot')
async def ping(ctx):
        await client.say("i refuse to respond pong this is 2019 check your privilage")

@client.command(pass_context=True, brief='allows owner to change the playing status', description='allows owner to change the playing status')
async def game(ctx, arg):
        if ctx.message.author.id == ownerid:
         await client.say("Setting game to " + arg)
         print('Game set to '+ arg)
         with open('lastgame.txt', 'w') as file:
          file.write(arg)
         file.close()
         await client.change_presence(game=discord.Game(name=arg))

@client.command(pass_context=True, brief='posts the dominos miku ad', description='posts the dominos miku ad')
async def dominos(ctx):
    await client.say("have some fucking fun with miku https://www.youtube.com/watch?v=UVV95JQcWhg")

@client.command(pass_context=True, brief='forces stoph and rei to work on the bot', description='forces stoph and rei to work on the bot')
async def work(ctx):
    await client.say("oof this command isnt implemented yet, you can make it tho if u want: https://github.com/reitraced/reibot9000")


@client.command(pass_context=True, brief='posts a link to the source code', description='posts a link to the source code')
async def source(ctx):
    await client.say('https://github.com/reitraced/reibot9000')

@client.command()
async def joined(member : discord.Member):
    """says when someone joined"""
    await client.say('{0.name} joined this server on {0.joined_at}'.format(member))

@client.command(pass_context=True, brief='displays credits')
async def credits(ctx):
    await client.say('**REIBOT9000 CREDITS**')
    await client.say('ALL THE USEFUL SHIT: stophman1')
    await client.say('ALL THE USELESS SHIT: reitraced')


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
            print('Loaded {}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))


client.run(token)
