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
            'ouro': 0
        }

    estado_do_jogador = estados[partidas[autor]['estado']]
    inventario_do_jogador = partidas[autor]['inventario']

    for key, value in estado_do_jogador['proximos_estados'].items():
        if fullmatch(key, msg.content):
            if inventario_do_jogador.issuperset(estados[value]['inventario']):
                # Atualiza o estado do jogador
                partidas[autor]['estado'] = value
                partidas[autor]['vida'] += estado_do_jogador['vida']
                partidas[autor]['ouro'] += estado_do_jogador['ouro']
                # Remove os itens de inventário requisitados
                partidas[autor]['inventario'] = inventario_do_jogador.difference(
                    estados[value]['inventario'])
                # Mostra a vida de forma "automatica" em cada estado diferente de 0
                if partidas[autor]['vida'] >=100:
                    partidas[autor]['vida'] = 100           
                if partidas[autor]['estado'] != 0:
                    await msg.channel.send("vida: "+str(partidas[autor]['vida']))
                    await msg.channel.send('Ouro: '+str(partidas[autor]['ouro']))
                hit = randint(0,100)
                if partidas[autor]['estado'] == 2:
                    if hit <= 85:
                        await msg.channel.send('Acertou, derrotando o monstro e ganhando 15 peças de ouro {avançar}')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 20 de vida! {Atacar/fugir}')
                        partidas[autor]['estado'] = 1
                if partidas[autor]['estado'] == 14:
                    if hit <= 85:
                        await msg.channel.send('Acertou!')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 10 de vida! {Atacar/fugir}')
                        partidas[autor]['estado'] = 12
                        # NAO ESTA FUNCIONANDO, FAZER UM INTERMEDIÁRIO ENTRE O ESTADO 12 E 14!!!
                if partidas[autor]['estado'] == 12:
                    if hit <= 85:
                        await msg.channel.send('Acertou!')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 30 de vida! {Atacar/fugir}')
                        partidas[autor]['estado'] = 12
                escapar = randint(0,100)
                if partidas[autor]['estado'] == 3:
                    if escapar <= 75:
                        await msg.channel.send('Conseguiu escapar! {avançar}')
                        partidas[autor]['estado'] = 2
                    else:
                        await msg.channel.send('Não escapou')
                        partidas[autor]['estado'] = 1
                if partidas[autor]['estado'] == 13:
                    if escapar <= 75:
                        await msg.channel.send('Conseguiu escapar! {avançar}')
                        partidas[autor]['estado'] = 15
                    else:
                        await msg.channel.send('Não escapou')
                        partidas[autor]['estado'] = 10
                if partidas[autor]['estado'] == 17:
                    await msg.channel.send('Chegando na ferraria, o ferreiro anuncia: "Se tocar tem que comprar, estou cansado de forasteiros vindo na minha ferraria e quebrando ou roubando minhas mercadorias!')
                    await msg.channel.send('Itens: escudo "seminovo" por 20 peças de ouro (5 de negação de dano) e espada enferrujada por 28 peças de ouro(40 de dano). {escudo/espada/voltar}')

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