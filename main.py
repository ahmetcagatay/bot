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
    
    if "!help" == mesaj:
        embed=discord.Embed(title="Yardım / Help", description="!komutlar ile sahip olduğum özellikleri tek bir listede görüntüleyebilirsin.")
        embed.set_author(name="Enigma")
        embed.add_field(name="Dil:", value="%100 Türkçe", inline=False)
        embed.add_field(name="Yazılım:", value="Açık Kaynak (Github)", inline=False)
        embed.add_field(name="Yüklenmiş Özellik Sayısı:", value="5", inline=False)
        embed.add_field(name="Bulunan Sunucu Sayısı:", value="4", inline=True)
        embed.set_footer(text="Enigma, Python dili ile yazılmış açık kaynaklı bir Discord botudur.")
        await message.channel.send(embed=embed)

    if "!yardım" == mesaj:
        embed=discord.Embed(title="Yardım / Help", description="!komutlar ile sahip olduğum özellikleri tek bir listede görüntüleyebilirsin.")
        embed.set_author(name="Enigma")
        embed.add_field(name="Dil:", value="%100 Türkçe", inline=False)
        embed.add_field(name="Yazılım:", value="Açık Kaynak (Github)", inline=False)
        embed.add_field(name="Yüklenmiş Özellik Sayısı:", value="5", inline=False)
        embed.add_field(name="Bulunan Sunucu Sayısı:", value="4", inline=True)
        embed.set_footer(text="Enigma, Python dili ile yazılmış açık kaynaklı bir Discord botudur.")
        await message.channel.send(embed=embed)
        

bot.run(to+ke+n)
