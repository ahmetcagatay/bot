import discord
# Discord kütüphanesinden komut bölümü uygulama içine alındı.
from discord.ext import commands

# Komut özelliğinden yararlanılarak Discord botunun önismi ayarlandı.
bot = commands.Bot(command_prefix='!')

@bot.event # Bot için event belirlendi.
async def on_ready(): #Bot hazır olduğunda yapılacak işlemler için fonksiyon belirlendi.
    print(f'{bot.user.name} artık aktif!') # Botun aktif olduğunda komut istemcisine ismi ile birlikte aktif olduğunu belirten bir yazı gönderilecek.
    await bot.change_presence(activity=discord.Game(name="!yardım"))


to = "NzE0MjA1ODc0NzA0NDgyMzc1"
ke = ".XsrSDQ."
n = "xYJQ9jwMnniLzktRKX5HiD487vc"


bot.run(to+ke+n)