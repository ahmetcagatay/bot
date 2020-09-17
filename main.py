import discord
import os
import random
import discord
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands

# Komut özelliğinden yararlanılarak Discord botunun önismi ayarlandı.
bot = commands.Bot(command_prefix='!')

@bot.event # Bot için event belirlendi.
async def on_ready(): #Bot hazır olduğunda yapılacak işlemler için fonksiyon belirlendi.
    print(f'{bot.user.name} artık aktif!') # Botun aktif olduğunda komut istemcisine ismi ile birlikte aktif olduğunu belirten bir yazı gönderilecek.
    await bot.change_presence(activity=discord.Game(name="Ich bin Enigma"))


to = "NzU0NzA4NjUyNzA2"
ke = "NzU4NzI4.X14rNA.SyDYn8-"
n = "P5bHsWb_kYyDvh5QVtcQ"

import wiki
import turkdil

@bot.event #Bot için event belirlendi.
async def on_message(message): # Mesajlaşma sırasında yapılacaklar belirtildi.
    if message.author == bot.user: 
        return

    mesaj = message.content.lower()

    if "!w" in mesaj:
        await wiki.resarch(mesaj, message)
    if "!tdk" in mesaj:
        await turkdil.tdkara(mesaj, message)
    
    if "!help" or "!yardım"== mesaj:
        embed=discord.Embed(title=Yardım..., description="!komutlar ile sahip olduğum komutlar listesine bakabilirsiniz.", color=0xdd2c2c)
        embed.set_author(name="Enigma", url="https://www.google.com.tr", icon_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fen%2Fthumb%2F8%2F80%2FWikipedia-logo-v2.svg%2F1200px-Wikipedia-logo-v2.svg.png&f=1&nofb=1")
        embed.set_footer(text="Enigma; Python ile yazılmış, açık kaynaklı bir discord botu")
        await message.channel.send(embed=embed)

bot.run(to+ke+n)
