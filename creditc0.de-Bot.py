# Created by creditc0.de
# with 💙 
# Built with the discord.py API
# Have fun!

import random
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from random import choice

Client = discord.Client()
bot_prefix="."
client = commands.Bot(command_prefix=bot_prefix)

chat_filter = ["NIGGER", "SKID", "PENIS"]
bypass_list = []

@client.event
async def on_ready():
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print('---------------------------------------')
	print("Created by creditc0.de with 💙  and the \ndiscord.py API!")
	await client.change_presence(game=discord.Game(name='created by creditc0.de'))

@client.command(pass_context=True)
async def src(ctx):
    embed = discord.Embed(title = "Get the source here: \n http://github.com/CreditCode ", color = 0xFFFFF)
    return await client.say(embed = embed)

@client.command(pass_context=True)
async def memes(ctx):
	await client.say("insert meme here")
	
@client.command(pass_context = True)
async def ban(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return
 
    if not member:
        return await client.say(ctx.message.author.mention + "Tell me a member!")
    try:
        await client.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":( You can't ban that Person!")
 
    embed = discord.Embed(description = "**%s** has been banned!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)

@client.command(pass_context = True)
async def getbans(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "Banned Members: ", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

@client.command(pass_context=True)       
async def clear(ctx, number):
    mgs = []
    number = int(number) 
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)

client.run("123456789") # this isn't a real id
