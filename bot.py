import discord 
from discord.ext import commands 

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")
   
@bot.event
async def on_member_join(member):
    print(f"{member} join my server! omg , is that even possible (just kidding)")

@bot.event
async def on_member_remove(member):
    print(f"{member} leavemy server... QAQ , this is so sad")    

bot.run('NzM1MDU0MDk5NDAxMTQ2NDMw.Xxaqng.O5VULPinfNbInF2y2K8tuEgDXb8')   