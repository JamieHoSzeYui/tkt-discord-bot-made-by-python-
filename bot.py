import discord 
from discord.ext import commands 
import json 
import random as r
import math
import urllib.parse
import re
import urllib.request




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

@bot.command()
async def dice(ctx):
    player_point=r.randint(1,6)
    bot_point=r.randint(1,6)
    await ctx.send(f'{ctx.author} dice **{player_point}** \n gay ryan dice **{bot_point}**')
    if(player_point>bot_point):
        await ctx.send(f'you win!')
    elif(player_point<bot_point):
        await ctx.send(f'you lose hahahaha')        

@bot.command()
async def sub(ctx):
    player_sub=r.randint(1,6)
    if(player_sub == 1):
        await ctx.send(f'{ctx.author} , you can subscribe **just go travel** ! \n "own the world without travel!"  \n link: https://www.youtube.com/channel/UCazYt7aApTjNOkPtacztKhg ')
    elif(player_sub == 2):
        await ctx.send(f'want to watch rubbish video? \n {ctx.author} ,  **tkt0506** is a suck channel for you! \n link: https://www.youtube.com/channel/UCeFtECVoP1XLwoH9kopKD6w ')    
    elif(player_sub == 3):
        await ctx.send(f'looking forward to watch Brawl Stars hack? \n{ctx.author} , go watch  **professor yeung** ~ \n link: https://www.youtube.com/channel/UCVF-qjWp7xWQkHQXh9rv_wA ')
    elif(player_sub == 4):
        await ctx.send(f'csgo or roblox? {ctx.author} , **dizziryhos** is a ~~gay~~ (just kidding) ! \n link: https://www.youtube.com/channel/UC39KTv488nBhHLOG3LajvYw ') 
    elif(player_sub == 5):
         await ctx.send(f'{ctx.author} , you can subscribe **Wiley** ! \n link: sry Wiley i lost it QAQ ') 
    elif(player_sub == 6): 
         await ctx.send(f'{ctx.author} , you can do not subscribe **gundam** ! \n link: i forgot as i did not subscribe hahaha ') 

@bot.command()
async def helpme(ctx):
    await ctx.send(f'hello {ctx.author} , i have ~~not~~ many fuction \n type **[sub** to know what you can watch \n type **[dice** to play with my with a dice \n type **[ping** to know my ping , also you can type **[round_ping** to round off the ping \n if you have any problem , you can contact @tkt0506 !')         

@bot.command()
async def test(ctx , arg):
    await ctx.send(arg)

@bot.command()
async def add(ctx , a:int):
  await ctx.send( a * 2 )

@bot.command()
async def dectobin(ctx , a:int):
  answer = bin( a )
  await ctx.send(f'the answer is **{answer}**')

@bot.command()
async def dectohex(ctx , a : int):
  answer = hex( a )
  await ctx.send(f'the answer is **{answer}**')

@bot.command()
async def youtube(ctx , *, search):
    query_string = urllib.parse.urlencode({
        'search_query' : search
    })
    htm_content = urllib.request.urlopen(
        'https://www..youtube.com/results?' + query_string
    )
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})' , htm_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

       
bot.run('NzM1MDU0MDk5NDAxMTQ2NDMw.XxaqeQ.UkTo-RCUdzNcYChHaZArI3BAalQ')   