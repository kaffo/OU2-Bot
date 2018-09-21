import asyncio
import discord
from discord.ext import commands
from shutil import copy2
import os
import json
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

def check_campaign_exists(campaign_name):
    files = os.listdir('data\\')
    for file in files:
        file_name = file.split('.')[0]
        if (file_name == campaign_name):
            return True
    return False

async def new_campaign(ctx, campaign_name):
    if (check_campaign_exists(campaign_name)):
        await bot.send_message(ctx.message.channel, campaign_name + ' already exists! Use a new name')
        return
    print("Creating new campaign with name: " + str(campaign_name))
    copy2('data\\template.json', 'data\\' + campaign_name + '.json')
    await bot.send_message(ctx.message.channel, campaign_name + ' has been created! :tada:')

@bot.command(pass_context=True)
async def campaign(ctx, campaign_type = None, campaign_name = None):
    if (campaign_type is None or campaign_name is None):
        await bot.send_message(ctx.message.channel, '```!campaign [new|status] ["name"]```')
        return

    if (campaign_type == 'new'):
        await new_campaign(ctx, campaign_name)
    else:
        await bot.send_message(ctx.message.channel, 'More coming soon... :star2:')

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
