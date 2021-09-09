import discord
from discord.ext import commands
import os
import sys

description = '''El Lil Bot'''
TOKEN = os.environ.get('TOKEN')
    
if TOKEN == None:
    sys.exit('Error, no token')
else:
    print (f'TOKEN is in the house')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def sumar(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeti(ctx, times: int = 0, *content): #='repetir que? cateto!'
    """Repeats a message multiple times."""
    if times == 0:
        await ctx.send('cuantes veces? cateto!')
        return
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def cuando(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} Entro el {0.joined_at}'.format(member))

@bot.command()
async def colega(ctx, member: discord.Member):
    """Si es un colega lil.."""
    print (member.name)
    if "ŁIL" in member.name:
        await ctx.send('{0.name} Es miembro de ŁIL Army. 1st class!'.format(member))
    else:
        await ctx.send('{0.name} Es un miembro de segunda clase'.format(member))

        
        
@colega.error
async def colega_handler(ctx, error):
    """A local Error Handler for our command do_repeat.
    This will only listen for errors in do_repeat.
    The global on_command_error will still be invoked after.
    """

    if isinstance(error, commands.MemberNotFound):
        await ctx.send("Y ese quien es?")
    else:
        await ctx.send(f"no se que paso bro.. {error}")


@bot.command()
async def info(ctx: commands.Context, user: discord.User):
    # In the command signature above, you can see that the `user`
    # parameter is typehinted to `discord.User`. This means that
    # during command invocation we will attempt to convert
    # the value passed as `user` to a `discord.User` instance.
    # The documentation notes what can be converted, in the case of `discord.User`
    # you pass an ID, mention or username (discrim optional)
    # E.g. 80088516616269824, @Danny or Danny#0007

    # NOTE: typehinting acts as a converter within the `commands` framework only.
    # In standard Python, it is use for documentation and IDE assistance purposes.

    # If the conversion is successful, we will have a `discord.User` instance
    # and can do the following:
    print("debug...")
    user_id = user.id
    username = user.name
    avatar = user.avatar.url
    await ctx.send(f'Encontrao el pana: {user_id} -- {username}\n{avatar}')

@info.error
async def info_error(ctx: commands.Context, error: commands.CommandError):
    # if the conversion above fails for any reason, it will raise `commands.BadArgument`
    # so we handle this in this error handler:
    if isinstance(error, commands.BadArgument):
        return await ctx.send('Y ese quien es?')



@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')
    
@bot.command()
async def ping(ctx):
    print('ping!')
    await ctx.send('pong - ŁIL Luzzybot version 0.1 beta')


@bot.command(pass_context=True)
async def cambiale(ctx, member: discord.Member, nuevo):
    # print (f'queriendo cambiar a {nuevo}')
    # await member.edit(nick=nuevo)
    await ctx.send(f'Este comando esta deshabilitado {member.mention}, se cambia automatico cuando entran!')
    

@bot.event
async def on_member_join(member):
    actual_nick = str(member.display_name)
    if "ŁIL " in actual_nick:
        for channel in member.guild.channels:
            if str(channel) == "tonterias":
                await channel.send(f"""Bienvenido, tu ya eres un ŁIL que guay! {member.mention}!""")
    else:
        nuevo=f'ŁIL {actual_nick}'
        await member.edit(nick=nuevo)
        for channel in member.guild.channels:
            if str(channel) == "tonterias":
                await channel.send(f"""Bienvenido a ŁIL Army {actual_nick}, te hemos cambiado el nick a {member.mention}""")
        
    
    
bot.run(TOKEN)
