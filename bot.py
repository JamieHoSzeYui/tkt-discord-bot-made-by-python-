import discord 
from discord.ext import commands 

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")
   

bot.run('NzM1MDU0MDk5NDAxMTQ2NDMw.Xxaqng.O5VULPinfNbInF2y2K8tuEgDXb8')   