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
        # Jogador começa com os itens abaixo
        partidas[autor] = {
            'estado': 0,
            'inventario': {
                'bomba_de_fumaça',
                'espada_quebrada',
                'poção_de_cura'
            },
            'vida': 0,
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
                # Mostra a vida de forma "automatica" em cada estado diferente de 0
                if partidas[autor]['vida'] >=100:
                    partidas[autor]['vida'] = 100
                if partidas[autor]['vida'] <=0:
                    partidas[autor]['estado'] = 0              
                if partidas[autor]['estado'] != 0:
                    await msg.channel.send("vida: "+str(partidas[autor]['vida']))
                if partidas[autor]['estado'] == 2:
                    hit = randint(0,100)
                    if hit <= 1:
                        await msg.channel.send('Acertou! {avançar}')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 25 de vida! {Atacar/fugir}')
                        partidas[autor]['estado'] = 1
                if partidas[autor]['estado'] == 3:
                    escapar = randint(0,100)
                    if escapar <= 50:
                        await msg.channel.send('Conseguiu escapar')
                        partidas[autor]['estado'] = 4
                    else:
                        await msg.channel.send('Não escapou')
                        partidas[autor]['estado'] = 1

                if partidas[autor]['vida'] <= 0:
                    await msg.channel.send('Você infelizmente morreu... Vamos voltar do começo!')
                    partidas[autor]['estado'] = 0

                await msg.channel.send(choice(estados[value]['frases']))
            else:
                await msg.channel.send(frases['inventario_insuficiente'])
            return
    if partidas[autor]['estado'] == 0:
        await msg.channel.send(choice(estado_do_jogador['frases']))
    else:
        await msg.channel.send(frases['erro'])
bot.run(getenv('DISCORD_TOKEN'))