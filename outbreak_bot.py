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
    embed.add_field(name="Python", value="3.6.5", inline=True)
    embed.add_field(name="About OU2", value="This bot helps with Outbreak Undead 2E PbP games on Discord", inline=False)
    embed.set_footer(text="Kaffo 2018")
    await bot.send_message(ctx.message.channel, embed=embed)

@bot.command(pass_context=True)
async def roll(ctx, *args):
    if (len(args) < 1):
        await bot.send_message(ctx.message.channel, '```!roll [# speed die] [# black die] [# damage die]```')
        return
    try:
        speed_num = int(args[0])
    except:
        speed_num = None
    print(speed_num)
    if (speed_num is None) or (type(speed_num) is int and speed_num < 1):
        await bot.send_message(ctx.message.channel, '```!roll [# speed die] [# black die] [# damage die]```')
        return
    speed_dice = random.randint(1, 6)
    percentile = random.randint(0, 99)
    await bot.send_message(ctx.message.channel, 'Your speed is ' + str(speed_dice) + ' and you rolled ' + str(percentile))

bot.run('key')
