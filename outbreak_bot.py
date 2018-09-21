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

async def generate_roll_embed(ctx, speed, percentile, diff, dam, dep):
    speed_embed = None
    percent_embed = None
    damage_embed = None
    deplete_embed = None

    if (len(speed) > 0):
        speed_embed = str(speed[0])
        total = speed[0]
        for roll in speed[1:]:
            speed_embed += ' + ' + str(roll)
            total += roll
        speed_embed += ' = **__' + str(total) + '__**'

    if (len(diff) > 0):
        percent_embed = '__' + str(percentile) + '__ + ' + str(diff[0])
        total = percentile + diff[0]
        for roll in diff[1:]:
            percent_embed += ' + ' + str(roll)
            total += roll
        percent_embed += ' = **__' + str(total) + '__**'
    else:
        percent_embed = '**__' + str(percentile) + '__**'

    if (len(dam) > 0):
        damage_embed = str(dam[0])
        total = dam[0]
        for roll in dam[1:]:
            damage_embed += ' + ' + str(roll)
            total += roll
        damage_embed += ' = **__' + str(total) + '__**'

    if (len(dep) > 0):
        deplete_embed = str(dep[0])
        total = dep[0]
        for roll in dep[1:]:
            deplete_embed += ' + ' + str(roll)
            total += roll
        deplete_embed += ' = **__' + str(total) + '__**'
        
    embed=discord.Embed(color=0xff7171)
    if (speed_embed is not None):
        embed.add_field(name="Speed", value=speed_embed, inline=True)
    embed.add_field(name="Percentile", value=percent_embed, inline=True)
    if (damage_embed is not None):
        embed.add_field(name="Damage", value=damage_embed, inline=True)
    if (deplete_embed is not None):
        embed.add_field(name="Depletion", value=deplete_embed, inline=True)
    await bot.send_message(ctx.message.channel, embed=embed)

@bot.command(pass_context=True)
async def roll(ctx, *args):
    if (len(args) < 4):
        await bot.send_message(ctx.message.channel, '```!roll [# speed die] [# difficulty die] [# damage die] [# depletion die]```')
        return
    try:
        speed_num = int(args[0])
        diff_num = int(args[1])
        dam_num = int(args[2])
        dep_num = int(args[3])
    except:
        speed_num = None
        diff_num = None
        dam_num = None
        dep_num = None
        
    print('speed: ' + str(speed_num) + ' diff: ' + str(diff_num) + ' dam: ' + str(dam_num) + ' dep: ' + str(dep_num))
    if (speed_num is None) or (diff_num is None) or (dam_num is None) or (dep_num is None):
        await bot.send_message(ctx.message.channel, '```!roll [# speed die] [# difficulty die] [# damage die] [# depletion die]```')
        return
    if (speed_num < 1 or diff_num < 0 or dam_num < 0 or dep_num < 0):
        await bot.send_message(ctx.message.channel, '```!roll [# speed die] [# difficulty die] [# damage die] [# depletion die]```')
        return

    percentile = random.randint(0, 99)
    speed_dice = []
    diff_dice = []
    dam_dice = []
    dep_dice = []

    for i in range(speed_num):
        speed_dice.append(random.randint(1, 6))
    for i in range(diff_num):
        diff_dice.append(random.randint(1, 6))
    for i in range(dam_num):
        dam_dice.append(random.randint(1, 6))
    for i in range(dep_num):
        dep_dice.append(random.randint(1, 6))
    
    await generate_roll_embed(ctx, speed_dice, percentile, diff_dice, dam_dice, dep_dice)

bot.run('key')
