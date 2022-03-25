import discord
import os
import sys
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import glob
# import PIL
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


def font(message, color_text="white", fontsize=40):
  text = message
  font ="Radiant"

  
  
    
  
  image = Image.open(IMG_OPEN_DIR + "/limit.png")
  print(PATH_DIR + '/fonts/{}.ttf'.format(font))
  font_type = ImageFont.truetype(PATH_DIR + '/fonts/{}.ttf'.format(font),fontsize)       

  draw = ImageDraw.Draw(image)
  draw.text(xy=(3,3),text=text,fill=("{}".format(color_text)),font=font_type)
  # import uuid
  # filename = str(uuid.uuid4())
  filename= 'test3'
  image.save(PATH_DIR + '/output/{}.png'.format(filename))
  # await bot.say("{} says:".format(ctx.message.author.mention))
  path = PATH_DIR + '/output/{}.png'.format(filename)
  # await bot.send_file(ctx.message.channel, path)

  
  fileCounter = len(glob.glob1(PATH_DIR + '/output/',"*.png"))
  print(fileCounter)
  if fileCounter > 1:
    print('hi')
    test = os.listdir(PATH_DIR + '/output/')
    for item in os.listdir(PATH_DIR + '/output/'):
      print('yep')
      if item.endswith(".png"):
        print(item)
        os.remove(PATH_DIR + '/output/'+ item)



font("Radiant")