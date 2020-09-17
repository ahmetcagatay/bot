
import discord
from tdk.core import TurkishWord

async def tdkara(mesaj, message):
    b= mesaj.split()
    if b[0] == '!tdk':
        del b[0]
    print(b)
    stringList2 = ' '.join([str(item) for item in b ])
    print(stringList2)
    word = TurkishWord(stringList2)
    word.query()
    result = word.meaning
    print(result)
    await message.channel.send(result)