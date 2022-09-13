from os import getenv
from dotenv import load_dotenv
import discord
load_dotenv()
from random import randint
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('#hello'):
            await message.reply('Salve', mention_author=True)
        if message.content.startswith('#atacar'):
            acerto = randint(0, 100)
            if acerto > 75:
                acerto = "Errou!"
            else:
                acerto = "Acertou!"
            await message.reply(acerto, mention_author=True)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(getenv("DISCORD_TOKEN"))