import discord
async def yardim():
    embed=discord.Embed(title="Yardım / Help", description="!komutlar ile sahip olduğum özellikleri tek bir listede görüntüleyebilirsin.")
    embed.set_author(name="Enigma")
    embed.add_field(name="Dil:", value="%100 Türkçe", inline=False)
    embed.add_field(name="Yazılım:", value="Açık Kaynak (Github)", inline=False)
    embed.add_field(name="Yüklenmiş Özellik Sayısı:", value="5", inline=False)
    embed.add_field(name="Bulunan Sunucu Sayısı:", value="4", inline=True)
    embed.set_footer(text="Enigma, Python dili ile yazılmış açık kaynaklı bir Discord botudur.")
    await message.channel.send(embed=embed)