from definições import frases, estados, partidas
import discord
from discord.ext import commands
from random import choice, randint
from re import fullmatch
from os import getenv
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='')


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.event
async def on_message(msg):
    # Testar se o autor é um bot (incluindo o próprio)
    if msg.author.bot:
        return

    autor = msg.author.id
    if autor not in partidas:
        # Jogador começa no estado 0 com duas chaves
        partidas[autor] = {
            'estado': 0,
            'inventario': {
                'bomba_de_fumaça',
                'espada_quebrada',
                'poção_de_cira'
            },
            'vida': 100,
        }

    estado_do_jogador = estados[partidas[autor]['estado']]
    inventario_do_jogador = partidas[autor]['inventario']

    for key, value in estado_do_jogador['proximos_estados'].items():
        if fullmatch(key, msg.content):
            if inventario_do_jogador.issuperset(estados[value]['inventario']):
                # Atualiza o estado do jogador
                partidas[autor]['estado'] = value
                partidas[autor]['vida'] += estado_do_jogador['vida']

                # Remove os itens de inventário requisitados
                partidas[autor]['inventario'] = inventario_do_jogador.difference(
                    estados[value]['inventario'])
                if partidas[autor]['estado'] ==1:
                    await msg.channel.send('Você encontrou um monstro no caminho e foi atacado! Atacar ou fugir?')
                    await msg.channel.send('Você recebeu dano, ficando com a vida de: ')
                    await msg.channel.send(estados[value]['vida'])

                if partidas[autor]['estado'] == 2:
                    hit = randint(0,100)
                    if hit <= 75:
                        await msg.channel.send('Acertou')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você da uma brexa para o inimigo te atacar e você morre, reiniciar?')
                    await msg.channel.send(estados[value]['vida'])
                if partidas[autor]['estado'] == 3:
                    escapar = randint(0,100)
                    if escapar <= 50:
                        await msg.channel.send('Conseguiu escapar')
                    else:
                        await msg.channel.send('Não escapou')
                await msg.channel.send(choice(estados[value]['frases']))
            else:
                await msg.channel.send(frases['inventario_insuficiente'])
            return

    if partidas[autor]['estado'] == 0:
        await msg.channel.send(choice(estado_do_jogador['frases']))
    else:
        await msg.channel.send(frases['erro'])

bot.run(getenv('DISCORD_TOKEN'))