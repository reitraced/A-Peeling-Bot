import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from asyncio import sleep
import sys
import random
import os

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

#@client.command(pass_context=True, brief='[Owner Only] Changes the current prefix.', description='[Owner Only] Changes the current prefix.')
#async def prefix(ctx, arg):
#        if ctx.message.author.id == ownerid:
#         await client.say("Setting prefix to " + arg)
#         print('Prefix set to '+ arg)
#         with open('prefix.txt', 'w') as file:
#          file.write(arg)
#         file.close()
#         os.execv('bot.py', sys.argv)

@client.command(pass_context=True, brief='posts the dominos miku ad', description='posts the dominos miku ad')
async def dominos(ctx):
    await client.say("have some fucking fun with miku https://www.youtube.com/watch?v=UVV95JQcWhg")

@client.command(pass_context=True, brief='forces stoph and rei to work on the bot', description='forces stoph and rei to work on the bot')
async def work(ctx):
    await client.say("oof this command isnt implemented yet, you can make it tho if u want: https://github.com/reitraced/reibot9000")

@client.command(pass_context=True, brief='posts reis twitch link', description='posts reis twitch link')
async def twitch(ctx):
    await client.say("lol my gay owners twitch is https://www.twitch.tv/last2livestream")
    await client.say("my much better and not gay twitch is https://www.twitch.tv/reibot9k :sunglasses:")

@client.command(pass_context=True, brief='posts reis steam link', description='posts reis steam link')
async def steam(ctx):
    await client.say('heres a gay steam account i found: https://www.steamcommunity.com/id/last2live')

@client.command(pass_context=True, brief='posts reis deviantart link', description='posts reis deviantart link')
async def deviantart(ctx):
    await client.say('heres a trash deviantart account: https://www.deviantart.com/reitrace')

@client.command(pass_context=True, brief='posts reis instagram link', description='posts reis instagram link')
async def instagram(ctx):
    await client.say('lol follow my insta: https://www.instagram.com/reitrace')

@client.command(pass_context=True, brief='posts a link to the source code', description='posts a link to the source code')
async def source(ctx):
    await client.say('https://github.com/reitraced/reibot9000')

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

@client.command(pass_context=True, brief='breaks out of jail')
async def jailbreak(ctx):
    await client.say('you attempt to organize a jailbreak with your cellmates, they are all for the idea. what they did not know was that the guards already knew and were waiting for the break. you are caught and ratted out as the organizer. you are sentenced to death. game over')

@client.command(pass_context=True, brief='finds all gay people on the server', description='finds all gay people on the server')
async def gaydetector(ctx):
    await client.say('REIBOT GAY DETECTOR ACTIVATED')
    await client.say('SCANNING')
    await sleep(5)
    await client.say('RESULTS: yall nibbas gay :joy:')

@client.command(pass_context=True, brief='guessing game', description='guess the correct number to win.')
async def guess(ctx):

        await client.say('guess a number between 1 to 10')

        def guess_check(m):
            return m.content.isdigit()

        guess = await client.wait_for_message(timeout=5.0, author=ctx.message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'lol u took too long what are u stupid its {}.'
            await client.say(fmt.format(answer))
            return
        if int(guess.content) == answer:
            await client.say('you got it right good job you win nothing good day')
        else:
            await client.say('lol you got gamered, it was actually {}.'.format(answer))

@client.command()
async def joined(member : discord.Member):
    """says when someone joined"""
    await client.say('{0.name} joined this server on {0.joined_at}'.format(member))

@client.command(pass_context=True, brief='check your rank', description='checks your server clout')
async def rank(ctx):
    await client.say('hell if i know ask mr owl or some shit idk')

@client.command(pass_context=True, brief='yeet', description='yeet')
async def yeet(ctx):
    await client.say('**y e e t**')

@client.command(pass_context=True, brief='rei is going to see the room at a theater', description='yes that was not a lie')
async def theroom(ctx):
    await client.say('oh hai mahk u very funny guy ahahahahaha')

@client.command(pass_context=True, brief='it is always right')
async def magicconch(ctx, *arg):
    if not arg:
        await client.say('lol u did not ask a question :rage:')
    else:
     ball8 = random.choice(['yea def gon happen','hell yea fam', 'oof not gonna happen', 'yea sure', 'def gonna happen i can see it im under your bed', 'never gonna happen', 'dont see it happening', 'my gamer sources say no', 'lol no', 'most likely gonna happen', 'you can rely on it', 'im too lazy to awnswer this right now'])
     await client.say(ball8)

@client.command(pass_context=True, brief='dick measurer')
async def pp(ctx):
    pp = random.choice(['long schlong :straight_ruler:', 'thicc dicc :eggplant:', 'teenie weenie :hotdog:', 'lol ur dick smol :joy:'])
    await client.say('REIBOT9000 PP MEASUREMENT TOOL ACTIVATED')
    await client.say('MEASURING.....')
    await sleep(2)
    await client.say("RESULTS: " + pp)

@client.command(pass_context=True, brief='tells reibot that its gay')
async def gay(ctx):
    await client.say('yeah you too')

@client.command(pass_context=True, brief='oof')
async def oof(ctx):
    await client.say('oof')

@client.command(pass_context=True, brief='rage command')
async def rage(ctx):
    await client.say('lol stop raging and get over it *dabs*')

@client.command(pass_context=True, brief='tells reibot to kill someone')
async def kill(ctx, *arg):
    await client.say('lol im not a hitman go get a gun and kill them yourself lazy bones')

@client.command(pass_context=True, brief='displays credits')
async def credits(ctx):
    await client.say('**REIBOT9000 CREDITS**')
    await client.say('ALL THE USEFUL SHIT: stophman1')
    await client.say('ALL THE USELESS SHIT: reitraced')

client.run(token)
