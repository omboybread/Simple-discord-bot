import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import random
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    print("bot online")

dick_size = random.randint(30,1500) #pp size in mm
dick_size2 = dick_size // 10
    
@client.command()
async def bread(ctx):
    await ctx.send("Hi! I am omboybreads personal bot. For now I can`t do much and will probablly not respond to you. But I will probablly get improved! :)")

@client.command()
async def Eat(ctx):
    await ctx.send("dick") 


@client.command()
async def pp_size(ctx):
  dick_size = random.randint(30,1500) #resets lenght
  await ctx.send("Your pp size is " + str(dick_size) + "mm!")





async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention)
    except:
        await ctx.send("bot does not have the kick members permission!")


client.run(os.getenv("TOKEN")) 