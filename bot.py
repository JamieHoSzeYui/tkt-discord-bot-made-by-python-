import discord 
from discord.ext import commands 

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")
   
@bot.event
async def on_member_join(member):
    print(f"{member} join my server! omg , is that even possible (just kidding)")
    channel = bot.get_channel(710883854680064064)
    await channel.send(f"{member} join my server! omg , is that even possible (just kidding)")

@bot.event
async def on_member_remove(member):
    print(f"{member} leave my server... QAQ , this is so sad")    
    channel = bot.get_channel(710883854680064064)
    await channel.send(f"{member} leav emy server... QAQ , this is so sad")

@bot.command()
async def ping(ctx):
    await ctx.send(f"{bot.latency*1000}(ms)")

@bot.command()
async def round_ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}(ms)")

bot.run('NzM1MDU0MDk5NDAxMTQ2NDMw.Xxa4Rw.JUek-FXhs9cYi0sbpGvqY_M1Wrc')   