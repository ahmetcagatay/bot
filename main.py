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
    await bot.change_presence(activity=discord.Game(name="Şifre Çözüyor"))


to = "NzU0NzA4NjUyNzA2"
ke = "NzU4NzI4.X14rNA.SyDYn8-"
n = "P5bHsWb_kYyDvh5QVtcQ"

import wiki

@bot.event #Bot için event belirlendi.
async def on_message(message): # Mesajlaşma sırasında yapılacaklar belirtildi.
    if message.author == bot.user: 
        return
    mesaj = message.content.lower()
    if "!w" in mesaj:
        await wiki.resarch(mesaj, message)
        
bot.run(to+ke+n)
