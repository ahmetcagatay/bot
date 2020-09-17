#wikipedia.py
import wikipedia
import json
import discord
wikipedia.set_lang("tr")
async def resarch(mesaj, message):
    a= mesaj.split()
    if a[0] == '!w':
        del a[0]
        print(a)
        stringList = ' '.join([str(item) for item in a ])
        print(stringList)
        ad = wikipedia.summary(stringList, sentences=2)
        kelime = "Aradığınız konu: "+stringList
        embed=discord.Embed(title=kelime, description=ad, color=0xdd2c2c)
        embed.set_author(name="Wikipedia", url="https://tr.wikipedia.org/", icon_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fen%2Fthumb%2F8%2F80%2FWikipedia-logo-v2.svg%2F1200px-Wikipedia-logo-v2.svg.png&f=1&nofb=1")
        embed.set_footer(text="!komutlar yazarak komut listesine ulaşabilirsiniz.")
        await message.channel.send(embed=embed)
    else:
        print("Yanlış yazım")
