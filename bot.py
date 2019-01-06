import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from asyncio import sleep
import sys

ownerid = "OWNER_ID_HERE"
p = "r!"
client = commands.Bot(command_prefix=p)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(pass_context=True, brief='Responds \'Poing!\'.', description='Responds \'Poing!\', This command is used for testing the bot.')
async def ping(ctx):
        await client.say("Pong!")

@client.command(pass_context=True, brief='[Owner Only] Changes the current game.', description='[Owner Only] Changes the current game.')
async def game(ctx, arg):
        if ctx.message.author.id == ownerid:
         await client.change_presence(game=discord.Game(name=arg))
         await client.say("Setting game to " + arg)

@client.command(pass_context=True, brief='posts the dominos miku ad', description='posts the dominos miku ad')
async def dominos(ctx):
    await client.say("have some fucking fun with miku https://www.youtube.com/watch?v=UVV95JQcWhg")

@client.command(pass_context=True, brief='forces stoph and rei to work on the bot', description='forces stoph and rei to work on the bot')
async def work(ctx):
    await client.say("why dont you work on the bot then, bozz")

@client.command(pass_context=True, brief='posts reis twitch link', description='posts reis twitch link')
async def twitch(ctx):
    await client.say("lol my gay owners twitch is https://www.twitch.tv/last2livestream")
    await client.say("my much better and not gay twitch is https://www.twitch.tv/reibot9k :sunglasses:")

@client.command(pass_context=True, brief='posts reis steam link', description='posts reis steam link')
async def steam(ctx):
    await client.say('heres a gay steam account i found: https://www.steamcommunity.com/id/last2live')

@client.command(pass_context=True, brief='nanners', description='nanners')
async def banana(ctx):
    await client.say("apples are better imo :apple:")

@client.command(pass_context=True, brief='red bed redemption', description='red bed redemption')
async def redbed(ctx):
    embed = discord.Embed()

    embed.set_image(url="https://i.imgur.com/EIBB5U3.png")

    await client.say(embed=embed)

@client.command(pass_context=True, brief='see how much money you have', description='see how much money you have')
async def currency(ctx):
    await client.say('you have no money as the economy is shit and you do not own any of the biggest corperations')

@client.command(pass_context=True, brief='find a job', description='find a job')
async def job(ctx):
    await client.say('you cannot get a job as no one is hiring, you live on the streets the rest of your life')

@client.command(pass_context=True, brief='commit crimes to earn money', description='commit criems to earn money')
async def crime(ctx):
    await client.say('in your attempt to rob the richest man in the galaxy, ignacious clerance weiner, you were caught and sentenced to 20 years of prison. look on the bright side, at least you have food now!')

@client.command(pass_context=True, brief='finds all gay people on the server', description='finds all gay people on the server')
async def gaydetector(ctx):
    await client.say('REIBOT GAY DETECTOR ACTIVATED')
    await client.say('SCANNING')
    await sleep(5)
    await client.say('RESULTS: yall nibbas gay :joy:')

client.run('BOT_TOKEN_HERE')
