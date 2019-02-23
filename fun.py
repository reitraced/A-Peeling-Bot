import discord
from discord.ext import commands
from asyncio import sleep
import random

class fun():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief='dick measurer')
    async def pp(self, ctx):
        pp = random.choice(['long schlong :straight_ruler:', 'thicc dicc :eggplant:', 'teenie weenie :hotdog:', 'lol ur dick smol :joy:'])
        await self.bot.say('REIBOT9000 PP MEASUREMENT TOOL ACTIVATED')
        await self.bot.say('MEASURING.....')
        await sleep(2)
        await self.bot.say("RESULTS: " + pp)

    @commands.command(pass_context=True, brief='see how much money you have', description='see how much money you have')
    async def currency(self, ctx):
        await self.bot.say('you have no money as the economy is shit and you do not own any of the biggest corperations')

    @commands.command(pass_context=True, brief='find a job', description='find a job')
    async def job(self, ctx):
        await self.bot.say('you cannot get a job as no one is hiring, you live on the streets the rest of your life')

    @commands.command(pass_context=True, brief='commit crimes to earn money', description='commit criems to earn money')
    async def crime(self, ctx):
        await self.bot.say('in your attempt to rob the richest man in the galaxy, ignacious clerance weiner, you were caught and sentenced to 20 years of prison. look on the bright side, at least you have food now!')

    @commands.command(pass_context=True, brief='breaks out of jail')
    async def jailbreak(self, ctx):
        await self.bot.say('you attempt to organize a jailbreak with your cellmates, they are all for the idea. what they did not know was that the guards already knew and were waiting for the break. you are caught and ratted out as the organizer. you are sentenced to death. game over')

    @commands.command(pass_context=True, brief='finds all gay people on the server', description='finds all gay people on the server')
    async def gaydetector(self, ctx):
        await self.bot.say('REIBOT GAY DETECTOR ACTIVATED')
        await self.bot.say('SCANNING')
        await sleep(5)
        await self.bot.say('RESULTS: yall nibbas gay :joy:')

    @commands.command(pass_context=True, brief='guessing game', description='guess the correct number to win.')
    async def guess(self, ctx):

            await self.bot.say('guess a number between 1 to 10')

            def guess_check(m):
                return m.content.isdigit()

            guess = await self.bot.wait_for_message(timeout=5.0, author=ctx.message.author, check=guess_check)
            answer = random.randint(1, 10)
            if guess is None:
                fmt = 'lol u took too long what are u stupid its {}.'
                await self.bot.say(fmt.format(answer))
                return
            if int(guess.content) == answer:
                await self.bot.say('you got it right good job you win nothing good day')
            else:
                await self.bot.say('lol you got gamered, it was actually {}.'.format(answer))

    @commands.command(pass_context=True, brief='yeet', description='yeet')
    async def yeet(self, ctx):
        await self.bot.say('**y e e t**')

    @commands.command(pass_context=True, brief='rei is going to see the room at a theater', description='yes that was not a lie')
    async def theroom(self, ctx):
        await self.bot.say('oh hai mahk u very funny guy ahahahahaha')

    @commands.command(pass_context=True, brief='it is always right')
    async def magicconch(self, ctx, *arg):
        if not arg:
            await self.bot.say('lol u did not ask a question :rage:')
        else:
         ball8 = random.choice(['yea def gon happen','hell yea fam', 'oof not gonna happen', 'yea sure', 'def gonna happen i can see it im under your bed', 'never gonna happen', 'dont see it happening', 'my gamer sources say no', 'lol no', 'most likely gonna happen', 'you can rely on it', 'im too lazy to awnswer this right now'])
         await self.bot.say(ball8)

    @commands.command(pass_context=True, brief='nanners', description='nanners')
    async def banana(self, ctx):
        await self.bot.say("apples are better imo :apple:")

    @commands.command(pass_context=True, brief='red bed redemption', description='red bed redemption')
    async def redbed(self, ctx):
        embed = discord.Embed()

        embed.set_image(url="https://i.imgur.com/EIBB5U3.png")

        await self.bot.say(embed=embed)

    @commands.command(pass_context=True, brief='check your rank', description='checks your server clout')
    async def rank(self, ctx):
        await self.bot.say('hell if i know im not mee6')

    @commands.command(pass_context=True, brief='tells reibot that its gay')
    async def gay(self, ctx):
        await self.bot.say('yeah you too')

    @commands.command(pass_context=True, brief='oof')
    async def oof(self, ctx):
        await self.bot.say('oof')

    @commands.command(pass_context=True, brief='rage command')
    async def rage(self, ctx):
        await self.bot.say('lol stop raging and get over it *dabs*')

    @commands.command(pass_context=True, brief='tells reibot to kill someone')
    async def kill(self, ctx):
        await self.bot.say('lol im not a hitman go get a gun and kill them yourself lazy bones')


def setup(bot):
    bot.add_cog(fun(bot))
