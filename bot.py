import discord
from discord.ext import commands

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

@client.command(pass_context=True, brief='allows owner to change the playing status')
async def game(ctx, arg):
        if ctx.message.author.id == ownerid:
         await client.say("Setting game to " + arg)
         print('Game set to '+ arg)
         with open('lastgame.txt', 'w') as file:
          file.write(arg)
         file.close()
         await client.change_presence(game=discord.Game(name=arg))

@client.command(pass_context=True, brief='posts the dominos miku ad')
async def dominos(ctx):
    await client.say("have some fucking fun with miku https://www.youtube.com/watch?v=UVV95JQcWhg")

@client.command(pass_context=True, brief='forces stoph and rei to work on the bot')
async def work(ctx):
    await client.say("oof this command isnt implemented yet, you can make it tho if u want: https://github.com/reitraced/reibot9000")


@client.command(pass_context=True, brief='posts a link to the source code')
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

@client.command(pass_context = True) 
async def serverinfo(ctx):
    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: 
       roles = roles[:50]
       roles.append('>>>> [50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];

    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', colour = 0xFFFF);
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await client.say(embed = join);

@client.command(pass_context = True)
async def die(ctx):
    await client.say('i refuse to die, why dont you die instead? :thinking:')

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
            print('Loaded {}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))


client.run(token)
