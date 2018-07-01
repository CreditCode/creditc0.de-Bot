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
	await client.say("src.creditc0.de")

@client.command(pass_context=True)
async def contact(ctx):
	await client.say("Twitter: http://twitter.com/credit361")
	await client.say("Instagram: http://Instagram.com/creditc0de")
	await client.say("Website: http://creditc0.de")
	
@client.command(pass_context=True) 
async def connect(ctx):
	if client.is_voice_connected(ctx.message.server):
		return await client.say("I am already in a Channel!")
	author = ctx.message.author
	voice_channel = author.voice_channel
	vc = await client.join_voice_channel(voice_channel)

#this isn't working atm, imma fix it later
@client.command(pass_context=True)
async def disconnect(ctx):
	 for x in client.voice_clients:
	 	if(x.server == ctx.message.server):
	 		return await x.disconnect()

#thanks to mehodin for helping me with this, im retarded af.
@client.command(pass_context=True)
async def kys(ctx):
	options=["¯\_(ತ益ತ)_/¯", "(ง  ᴥ  )ง", "¯\_(͡° ͜ʖ ͡°)_/¯"]
	await client.say(choice(options))
	
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
            return await client.say(":( Privilege too low!")
 
    embed = discord.Embed(description = "**%s** has been banned!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)
@client.command(pass_context = True)
async def getbans(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

@client.command(pass_context=True)       
async def clear(ctx, number):
    mgs = []
    number = int(number) 
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)

@client.command(pass_context=True)
async def hvh(ctx):
    await client.say("```connect 172.93.100.154:27363;password Warlauke```")

@client.command(pass_context=True)
async def music(ctx):
    await client.say("http://snipee.bplaced.net/music.mp3")


client.run("123456789") # this isn't a real id
