import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import PIL
from PIL import Image, ImageDraw, ImageFont
import os
import sys

debug_mode = True
bot = commands.Bot(command_prefix='$')
module_check = 'PIL' in sys.modules
proceed_font = False

#bot secret:
my_secret = os.environ['bot_key']

PATH_DIR = os.getcwd()
print(PATH_DIR)
IMG_OPEN_DIR = PATH_DIR


plus_enabled = True


client = discord.Client()
clear = os.system("clear")

@bot.event
async def on_ready():
  print("Mechbot is good to go.")
  print("Mechbot is running with the id: " + str(bot.user.id))

@bot.command()
async def say(ctx, message=None):
  await ctx.send(message)

@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)
  
bot.run(my_secret)