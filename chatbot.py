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
            'vida': 100,
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
                # Junta 5 variáveis e transforma em duas, pois o comando .send só aceita até duas variaveis diferentes
                vida_stats = 'Vida: '+ str(partidas[autor]['vida'])+ ' / '
                ouro_stats = 'Ouro: '+str(partidas[autor]['ouro'])
                if partidas[autor]['estado'] != 0:
                    await msg.channel.send(str(vida_stats+ouro_stats))

                hit = randint(0,100)
                if partidas[autor]['estado'] == 2:
                    if hit <= 85:
                        await msg.channel.send('Acertou, derrotando o monstro e ganhando 15 peças de ouro {avançar}')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 20 de vida! {Atacar/fugir}')
                        partidas[autor]['estado'] = 1
                if partidas[autor]['estado'] == 5:
                    partidas[autor]['inventario'].add('espada_enferrujada')
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
                        partidas[autor]['estado'] = 10
                escapar = randint(0,100)
                if partidas[autor]['estado'] == 3:
                    if escapar <= 95:
                        await msg.channel.send('Conseguiu escapar! {avançar}')
                        partidas[autor]['estado'] = 2
                    else:
                        await msg.channel.send('Não escapou')
                        partidas[autor]['estado'] = 1
                if partidas[autor]['estado'] == 13:
                    if escapar <= 95:
                        await msg.channel.send('Conseguiu escapar! Da distância, você consegue ver um vilarejo {ir/ignorar}')
                        partidas[autor]['estado'] = 15
                    else:
                        await msg.channel.send('Não escapou')
                        partidas[autor]['estado'] = 10
                if partidas[autor]['estado'] == 17:
                    await msg.channel.send('Chegando na ferraria, o ferreiro anuncia: "Se tocar tem que comprar, estou cansado de forasteiros vindo na minha ferraria e quebrando ou roubando minhas mercadorias!')
                    await msg.channel.send('Itens: escudo "seminovo" por 45 peças de ouro (10 de negação de dano). {comprar/voltar}')
                    #FAZER UM SISTEMA PARA A VENDA DE ITENS, COMO A ESPADA NO COMEÇO DO JOGO
                    #FAZER UM SISTEMA PARA A VENDA DE ITENS, COMO A ESPADA NO COMEÇO DO JOGO
                    #FAZER UM SISTEMA PARA A VENDA DE ITENS, COMO A ESPADA NO COMEÇO DO JOGO
                    #FAZER UM SISTEMA PARA A VENDA DE ITENS, COMO A ESPADA NO COMEÇO DO JOGO
                    #FAZER UM SISTEMA PARA A VENDA DE ITENS, COMO A ESPADA NO COMEÇO DO JOGO
                    #FAZER UM SISTEMA PARA A VENDA DE ITENS, COMO A ESPADA NO COMEÇO DO JOGO
                if partidas[autor]['estado'] ==18:
                    await msg.channel.send('Entrando na tenda do mago, ele diz que trabalha com alquimia e te mostra os itens disponíveis na sua loja!')
                    await msg.channel.send('Itens: Poção de cura (20 peças de ouro) // bomba de fumaça (40 peças de ouro) {vida/fumaça/voltar}')
                if partidas[autor]['estado'] ==18.1:
                    await msg.channel.send('Você pega a poção de cura e vai até o mago para pagar')
                    if partidas[autor]['ouro'] <= 19:
                        await msg.channel.send('Você não tem peças de ouro suficientes para comprar esse item!')
                        partidas[autor]['estado'] = 18
                    else:
                        await msg.channel.send('Com a quantidade de dinheiro em mãos, você paga o mago! {voltar}')
                        partidas[autor]['inventario'].add('poção_de_cura')
                if partidas[autor]['estado'] ==18.2:
                    await msg.channel.send('Você pega a bomba de fumaça e vai até o mago para pagar')
                    if partidas[autor]['ouro'] <= 39:
                        await msg.channel.send('Você não tem peças de ouro suficientes para comprar esse item!')
                        partidas[autor]['estado'] = 18
                    else:
                        await msg.channel.send('Com a quantidade de dinheiro em mãos, você paga o mago! {voltar}')
                        partidas[autor]['inventario'].add('bomba_de_fumaça')
                if partidas[autor]['estado'] ==20:
                    await msg.channel.send('Você pega o escudo e vai até o ferreiro para pagar.')
                    if partidas[autor]['ouro'] <= 44:
                        await msg.channel.send('Você não tem peças de ouro suficientes para comprar esse item!')
                        partidas[autor]['estado'] = 17
                    else:
                        await msg.channel.send('Com a quantidade de dinheiro em mãos, você paga o ferreiro! {voltar}')
                        partidas[autor]['inventario'].add('escudo_seminovo')
                if partidas[autor]['estado']==21:
                    await msg.channel.send(inventario_do_jogador)
                    partidas[autor]['estado']=16
                if partidas[autor]['estado'] ==23:
                    await msg.channel.send('Depois de uma grande caminhada por essa floresta, você começa a escutar vozes e é parado por três jacares que saíram em um rio próximo e estão estranhamente coordenados. De longe, você vê uma bruxa que parece estar controlando esses animais!')
                
                if partidas[autor]['vida'] <= 0:
                    await msg.channel.send('Você infelizmente morreu... Vamos voltar do começo!')
                    partidas[autor]['estado'] = 0
                if partidas[autor]['estado'] == 23.1:
                    if hit <= 90:
                        await msg.channel.send('Acertou!')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 20 de vida! {Atacar/fugir}')
                        partidas[autor]['estado'] = 23
                if partidas[autor]['estado'] ==23.2:
                    if escapar <= 95:
                        await msg.channel.send('Conseguiu escapar! {avançar}')
                        partidas[autor]['estado'] = 24
                    else:
                        await msg.channel.send('Não escapou')
                        partidas[autor]['estado'] = 23
                if partidas[autor]['estado'] ==23.4:
                    if escapar <= 95:
                        await msg.channel.send('Conseguiu escapar! {avançar}')
                        partidas[autor]['estado'] = 24
                    else:
                        await msg.channel.send('Não escapou')
                        partidas[autor]['estado'] = 23.1
                if partidas[autor]['estado'] ==23.6:
                    if escapar <= 95:
                        await msg.channel.send('Conseguiu escapar! {avançar}')
                        partidas[autor]['estado'] = 24
                    else:
                        await msg.channel.send('Não escapou')
                        partidas[autor]['estado'] = 23.3
                if partidas[autor]['estado'] == 23.3:
                    if hit <= 85:
                        await msg.channel.send('Acertou!')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 30 de vida! {Atacar/fugir}')
                        partidas[autor]['estado'] = 23.1
                if partidas[autor]['estado'] == 23.5:
                    if hit <= 85:
                        await msg.channel.send('Acertou!')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 30 de vida! {Atacar/fugir}')
                        partidas[autor]['estado'] = 23.3
                if partidas[autor]['estado'] == 23.8 or partidas[autor]['estado'] == 23.7:
                    partidas[autor]['inventario'].add('couro_de_jacaré')
                    partidas[autor]['inventario'].add('couro_de_jacaré')
                    partidas[autor]['inventario'].add('couro_de_jacaré')
                if partidas[autor]['estado'] == 24.1:
                    if hit <= 85:
                        await msg.channel.send('Acertou!')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 30 de vida! {Atacar/fugir}')
                        partidas[autor]['estado'] = 24
                if partidas[autor]['estado'] ==24.2:
                    if escapar <= 95:
                        await msg.channel.send('Conseguiu escapar! {avançar}')
                        partidas[autor]['estado'] = 26
                    else:
                        await msg.channel.send('Não escapou')
                        partidas[autor]['estado'] = 24
                if partidas[autor]['estado'] == 24.3:
                    if hit <= 85:
                        await msg.channel.send('Acertou!')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 30 de vida! {Atacar/fugir}')
                        partidas[autor]['estado'] = 24.1
                if partidas[autor]['estado'] ==24.4:
                    if escapar <= 95:
                        await msg.channel.send('Conseguiu escapar! {avançar}')
                        partidas[autor]['estado'] = 24.1
                    else:
                        await msg.channel.send('Não escapou')
                        partidas[autor]['estado'] = 26
                await msg.channel.send(choice(estados[value]['frases']))
            else:
                await msg.channel.send(frases['inventario_insuficiente'])
            return
    if partidas[autor]['estado'] == 0:
        await msg.channel.send(choice(estado_do_jogador['frases']))
    else:
        await msg.channel.send(frases['erro'])
bot.run(getenv('DISCORD_TOKEN'))