import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import PIL
from PIL import Image, ImageDraw, ImageFont
import os
import sys
import glob
import config

debug_mode = False
bot = commands.Bot(command_prefix='$')
module_check = 'PIL' in sys.modules
proceed_font = False

#bot secret:
#my_secret = os.environ['bot_key']

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
#   await bot.change_presence(activity=discord.Game('Radiant Black Video Game'))
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Radiant Black Podcast'))

# @bot.command(pass_context=True)
# async def say(ctx, message=None):
#   await ctx.send(message)


@bot.command(pass_context=True)
async def servers(ctx):
  activeservers = bot.guilds
  await ctx.send("connected on: " +str(len(activeservers)) + " servers")
  
  for guild in activeservers:  
    await ctx.send(guild.name)
    print(guild.name)

@bot.command(pass_context=True)
async def font(ctx, message, color_text="white", fontsize=60):
    text = message
    font ="Radiant"
    # await bot.delete_message(ctx.message)
    try:
        # 30 max unless you want text running over
        if len(text) >= 40:
            await ctx.send("I'm sorry that message is too long. **40** is maximum character count.")

        else:
            pass
            image = Image.open(IMG_OPEN_DIR + "/limit.png")
            fontrequest = font
            path = PATH_DIR + "/fonts/"
            from pathlib import Path
            font_check = Path(path + "{}.ttf".format(fontrequest))        
            if font_check.is_file():
                font_type = ImageFont.truetype(PATH_DIR + '/fonts/{}.ttf'.format(font),fontsize)
                draw = ImageDraw.Draw(image)
                draw.text(xy=(5,5),text=text,fill=("{}".format(color_text)),font=font_type)
                import uuid
                filename = str(uuid.uuid4())
                image.save(PATH_DIR + '/output/{}.png'.format(filename))
                await ctx.send("{} says:".format(ctx.message.author.mention))
                path = PATH_DIR + '/output/{}.png'.format(filename)
                # print(path)
                await ctx.send(file=discord.File(path))
                #File clean-up process 
                fileCounter = len(glob.glob1(PATH_DIR + '/output/',"*.png"))
                # print(fileCounter)
                if fileCounter > 10:
                  test = os.listdir(PATH_DIR + '/output/')
                  for item in os.listdir(PATH_DIR + '/output/'):
                    if item.endswith(".png"):
                      # print(item)
                      os.remove(PATH_DIR + '/output/'+ item)
                
              
            # else:
            #     font_type = ImageFont.truetype(PATH_DIR + '/fonts/downloaded_fonts/{}.ttf'.format(fontrequest),42)
            #     draw = ImageDraw.Draw(image)
            #     draw.text(xy=(5,5),text=text,fill=("{}".format(color_text)),font=font_type)
            #     import uuid
            #     filename = str(uuid.uuid4())
            #     image.save(PATH_DIR + 'fontbot/output/{}.png'.format(filename))
            #     await bot.send("{} says:".format(ctx.message.author.mention))
            #     path = PATH_DIR + 'fontbot/output/{}.png'.format(filename)
            #     await bot.send_file(ctx.message.channel, path)
            #     os.system("rm {}/fontbot/output/{}.png".format(path, filename))
    except OSError as e:
        if debug_mode == True:
            await ctx.send(e.strerror)
        await ctx.send("**Uh oh!** The font ``{}`` is not a font available.".format(fontrequest))
        await ctx.send("See ``$mech_help`` on how to use fontbot")

# @bot.command(pass_context=True)
# async def install(ctx, ttf_file, name):
#     await bot.delete_message(ctx.message)
#     try:
#         if name.isalpha() and len(name) <= 15:
#             if plus_enabled == True:
#                 path = PATH_DIR + 'fontbot/fonts/downloaded_fonts/"
#                 from pathlib import Path
#                 font_check = Path(path + "{}.ttf".format(name))
#                 if font_check.is_file():
#                     print("font already exists")
#                     await bot.send("Looks like that font already exists! Change the name or use {} in the command.".format(name))
#                 else:
#                     pass
#                     import urllib.request
#                     filename = path + "{}.ttf".format(name)
#                     print("Downloading {}...".format(name))
#                     urllib.request.urlretrieve(ttf_file, filename)
#                     print("Downloaded {}".format(name))
#                     await bot.send("**Congratulations!** The font {} has been successfully installed. To use do ``#font 'Message' {} Color``".format(name, name))
#             else:
#                 await bot.send("**Sorry!** This feature requires the Plus version.")
#         else:
#             await bot.send("Sorry, font name must only contain only alphanumerical characters and be under 15 characters..")

#     except OSError:
#             await bot.send("Error encountered. (112)")
    

@bot.command(pass_context=True)
async def status(ctx):
    embed = discord.Embed(title="Current Status", description="for Mech Bot", color=0x9b9b9b)
    if debug_mode == True:
        embed.add_field(name="Debug Mode", value=":warning: Currently Active, I'm probably being worked on right now", inline=False)
    else:
        pass
    embed.add_field(name="Server Status", value=":white_check_mark: I'm currently connected to the server.", inline=False)
    if module_check == False:
        embed.add_field(name="Module Import Status", value=":no_entry: Modules are currently not active. Please contact @martystoked!", inline=False)
    elif module_check == True:
        embed.add_field(name="Module Import Status", value=":white_check_mark: Modules are currently imported and running.", inline=False)       
    embed.add_field(name="Need any assistance?", value=":grey_question: DM @martystoked to ask any questions.", inline=False)
    embed.add_field(name="Bot Version", value="Current Bot Version: 1.0", inline=False)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def mech_help(ctx):
    embed = discord.Embed(title="Quick guide on how to use Mech Bot!", colour=discord.Colour(0x9b9b9b), description="This should give you the low-down and in's and outs of using the bot.")


    embed.add_field(name="Writing messages", value="If you want to write a message. It's simple.```\n$font \"Message\" Color(optional) Font_size(optional)``` \nPlease note, the default color (white) and font size (60) can be changed. \n If the font size is increased too large it will not display properly.")
    # embed.add_field(name="Installing new fonts", value="You can also use new fonts as well. The great thing is that each server has it's own folder on my server. Meaning you can install personal or custom fonts. This also means you can use custom names! ```\n $install [linkto.ttf] nameOfFont``` \n Make sure it's a ``.ttf`` file. We **DO NOT SUPPORT ANY OTHER FORMAT**!. This isn't our fault.")
    embed.add_field(name="Checking the status of the bot", value="Sometimes, the bot can go down for numerous reasons. You can quickly check the status of the bot by doing ```$status```")
    embed.add_field(name="Any questions?", value="@martystoked on Twiter or DM me here", inline=True)
    embed.add_field(name="Disclaimers:", value="Radiant font created by Nick Castillo (@AmazngNickanger on Twitter). \n\rAll rights, properties, and ownership of intellectual property are owned by Image comics, Kyle higgans, and all parties associated with the Radiant Black universe.\n\rThis is an unoffical fan created font. This font is not meant to be used for comercial use, proffit, or redistrubted for personal financial gain. Please out of respect for it's creator and the community of Radiant Black, use this font respecfully.")

    await ctx.send(embed=embed)


    # async def on_message(self, message):
    #     # we do not want the bot to reply to itself
    #     if message.author.id == self.user.id:
    #         return

    #     if message.content.startswith('$guess'):
    #         await message.channel.send('Guess a number between 1 and 10.')

#bot.run(my_secret)
bot.run(os.getenv("DISCORD_TOKEN"))



