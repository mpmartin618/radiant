# print('hello world')
import discord
import os
import sys
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import PIL
from PIL import Image, ImageDraw, ImageFont
# import uuid
debug_mode = True
# my_secret = os.environ['bot_key']
bot = commands.Bot(command_prefix='$')
module_check = 'PIL' in sys.modules
proceed_font = False

#Path to code:

PATH_DIR = os.getcwd()
print(PATH_DIR)
IMG_OPEN_DIR = PATH_DIR

def font(message, color_text="black", fontsize=40):
  text = message
  fontrequest="comicsans"
  
  image = PIL.Image.open(IMG_OPEN_DIR + "/limit.png")
  font_type = fontrequest
  path = PATH_DIR + "/fonts/"       

  draw = PIL.ImageDraw.Draw(image)
  draw.text(xy=(3,3),text=text,fill=("{}".format(color_text)),font=font_type)
  # import uuid
  # filename = str(uuid.uuid4())
  filename= 'test'
  image.save(PATH_DIR + '/output/{}.png'.format(filename))
  # await bot.say("{} says:".format(ctx.message.author.mention))
  path = PATH_DIR + '/output/{}.png'.format(filename)
  # await bot.send_file(ctx.message.channel, path)

font('test')