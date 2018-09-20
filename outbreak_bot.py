import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def info(ctx):
    embed=discord.Embed(color=0xff7171)
    embed.add_field(name="Python", value="3.6.4", inline=True)
    embed.add_field(name="discord.py", value="1.0.0a", inline=True)
    embed.add_field(name="About BlueTemp", value="This is an instance of BlueTemp, an open sorce Discord Bot created by RedstonedLife", inline=False)
    embed.set_footer(text="A Template downloaded from Github")
    await bot.send_message(ctx.message.channel, embed=embed)

@bot.command(pass_context=True)
async def roll(ctx, speed_num = None):
    print(speed_num)
    if (speed_num is None) or (type(speed_num) is not int) or (type(speed_num) is int and speed_num < 1):
        await bot.send_message(ctx.message.channel, '```!roll [# speed die] [# black die] [# damage die]```')
        return
    speed_dice = random.randint(1, 6)
    percentile = random.randint(0, 99)
    await bot.send_message(ctx.message.channel, 'Your speed is ' + str(speed_dice) + ' and you rolled ' + str(percentile))

bot.run('key')
