import discord
from parol import genirated_password

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Бот включен{client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('$generate'):
        simvol_len = message.content.split(" ")
        if len(simvol_len) == 2:
            try: 
                otvet = genirated_password(int(simvol_len[1]))
            except TypeError:
                otvet = genirated_password()
        else:
            otvet = genirated_password()
        await message.channel.send(otvet)
    else:
        await message.channel.send(message.content)




client.run("")
