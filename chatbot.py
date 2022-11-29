from definições import frases, estados, canais_de_voz
import discord
from discord.ext import commands
from random import choice, randint
from re import fullmatch
from os import getenv
from dotenv import load_dotenv
from os.path import exists
import pymongo

load_dotenv()


# Iniciar base de dados com as definições do jogo
usuario = getenv('MONGODB_USERNAME', default='')
senha = getenv('MONGODB_PASSWORD', default='')
cluster = getenv('MONGODB_CLUSTER', default='')
uri = ''.join(['mongodb+srv://', usuario, ':', senha, '@', cluster, '/?retryWrites=true&w=majority'])
mongo_client = pymongo.MongoClient(uri)
database = mongo_client.chatbot
#
# Partidas
partidas_db = database.partidas

intents = discord.Intents.default()
intents.message_content = True
prefix = '#'
bot = commands.Bot(intents=intents, command_prefix=prefix)


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.event
async def on_message(msg):
    # Testar se o autor é um bot (incluindo o próprio)
    if msg.author.bot:
        return
    if msg.content.strip()[0] == prefix:
        mensagem = msg.content.strip()[1:]
    else:
        return

    autor = msg.author.id

    if fullmatch('[rR]einiciar?', mensagem):
        #
        # Pesquisar e apagar o registro no banco - e informar o usuário
        partidas_db.find_one_and_delete({'jogador': autor})
        await msg.channel.send(frases['reiniciado'])
        return
    if fullmatch('[sS]ing it for me.?', mensagem):
        #
        # Fechar todos os canais de voz
        [await canais_de_voz[i].disconnect() for i in canais_de_voz.keys()]
        await msg.channel.send(frases['saindo'])
        return
    #
    # Garantir que o autor tem dados de partida
    if partidas_db.count_documents({'jogador': autor}) == 0:
        #
        # Jogador começa no estado 0 e inventário vazio
        partidas_db.insert_one({'jogador': autor, 'estado': 0})
    #
    # Coletar os dados persistentes de usuário
    partida = partidas_db.find_one({'jogador': autor})
    #
    # Testar se o canal é pvt (msg.channel.type.name == 'private')
    # e, se for, avisar o jogador e continua o jogo sem áudio
    if msg.channel.type.name == 'private':
        #
        # Avisar ao jogador apenas quando o estado for 0
        if partida['estado'] == 0:
            await msg.channel.send(frases['canal_privado'])
            await msg.channel.send(frases['sem_canal_de_voz'])
    #
    # Testar se a mensagem foi mandada em um chat de servidor
    # se sim, testar se o jogador está em canal de voz,
    # caso não esteja convidá-lo a entrar em um.
    if msg.channel.type.name != 'private':
        if msg.author.voice:
            if msg.guild.me not in msg.author.voice.channel.members:
                canais_de_voz[autor] = await msg.author.voice.channel.connect()
        else:
            await msg.channel.send(frases['sem_canal_de_voz'])
            return
    if autor not in partida:
        # Jogador começa com os itens abaixo
        partidas_db.insert_one({
            'jogador': autor,
            'estado': 0,
            'inventario': ['bomba_de_fumaça','espada_quebrada','poção_de_cura'],
            'vida': 100,
            'ouro': 0
        })

    partida = partidas_db.find_one({'jogador': autor})
    inventario_do_jogador = partida['inventario']

    for key, value in estado_do_jogador['proximos_estados'].items():
        if fullmatch(key, mensagem):
            if fullmatch(key, mensagem):
                #
                # Atualiza o estado do jogador
                partida = partidas_db.find_one_and_update(
                    {'jogador': autor},
                    {'$set': {'estado': value}},
                    return_document=pymongo.ReturnDocument.AFTER
            )
            if set(inventario_do_jogador).issuperset(set(partida['inventario'])):
                # Atualiza o estado do jogador
                partida['estado'] = value
                partida['vida'] += estado_do_jogador['vida']
                partida['ouro'] += estado_do_jogador['ouro']
                # Remove os itens de inventário requisitados
                partida['inventario'] = inventario_do_jogador.difference(
                    estados[value]['inventario'])
                # Mostra a vida de forma "automatica" em cada estado diferente de 0
                if partida['vida'] >=100:
                    partida['vida'] = 100
                # Junta 5 variáveis e transforma em duas, pois o comando .send só aceita até duas variaveis diferentes
                vida_stats = 'Vida: '+ str(partida['vida'])+ ' / '
                ouro_stats = 'Ouro: '+str(partida['ouro'])
                if partida['estado'] != 0:
                    await msg.channel.send(str(vida_stats+ouro_stats))

                hit = randint(0,100)
                if partida['estado'] == 2:
                    if hit <= 85:
                        await msg.channel.send('Acertou, derrotando o monstro e ganhando 15 peças de ouro {avançar}')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 20 de vida! {Atacar/fugir}')
                        partida['estado'] = 1
                if partida['estado'] == 5:
                    partida['inventario'].add('espada_enferrujada')
                if partida['estado'] == 14:
                    if hit <= 85:
                        await msg.channel.send('Acertou!')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 10 de vida! {Atacar/fugir}')
                        partida['estado'] = 12
                        # NAO ESTA FUNCIONANDO, FAZER UM INTERMEDIÁRIO ENTRE O ESTADO 12 E 14!!!
                if partida['estado'] == 12:
                    if hit <= 85:
                        await msg.channel.send('Acertou!')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 30 de vida! {Atacar/fugir}')
                        partida['estado'] = 10
                escapar = randint(0,100)
                if partida['estado'] == 3:
                    if escapar <= 95:
                        await msg.channel.send('Conseguiu escapar! {avançar}')
                        partida['estado'] = 2
                    else:
                        await msg.channel.send('Não escapou')
                        partida['estado'] = 1
                if partida['estado'] == 13:
                    if escapar <= 95:
                        await msg.channel.send('Conseguiu escapar! Da distância, você consegue ver um vilarejo {ir/ignorar}')
                        partida['estado'] = 15
                    else:
                        await msg.channel.send('Não escapou')
                        partida['estado'] = 10
                if partida['estado'] == 17:
                    await msg.channel.send('Chegando na ferraria, o ferreiro anuncia: "Se tocar tem que comprar, estou cansado de forasteiros vindo na minha ferraria e quebrando ou roubando minhas mercadorias!')
                    await msg.channel.send('Itens: escudo "seminovo" por 45 peças de ouro (10 de negação de dano). {comprar/voltar}')
                    #FAZER UM SISTEMA PARA A VENDA DE ITENS, COMO A ESPADA NO COMEÇO DO JOGO
                    #FAZER UM SISTEMA PARA A VENDA DE ITENS, COMO A ESPADA NO COMEÇO DO JOGO
                    #FAZER UM SISTEMA PARA A VENDA DE ITENS, COMO A ESPADA NO COMEÇO DO JOGO
                    #FAZER UM SISTEMA PARA A VENDA DE ITENS, COMO A ESPADA NO COMEÇO DO JOGO
                    #FAZER UM SISTEMA PARA A VENDA DE ITENS, COMO A ESPADA NO COMEÇO DO JOGO
                    #FAZER UM SISTEMA PARA A VENDA DE ITENS, COMO A ESPADA NO COMEÇO DO JOGO
                if partida['estado'] ==18:
                    await msg.channel.send('Entrando na tenda do mago, ele diz que trabalha com alquimia e te mostra os itens disponíveis na sua loja!')
                    await msg.channel.send('Itens: Poção de cura (20 peças de ouro) // bomba de fumaça (40 peças de ouro) {vida/fumaça/voltar}')
                if partida['estado'] ==18.1:
                    await msg.channel.send('Você pega a poção de cura e vai até o mago para pagar')
                    if partida['ouro'] <= 19:
                        await msg.channel.send('Você não tem peças de ouro suficientes para comprar esse item!')
                        partida['estado'] = 18
                    else:
                        await msg.channel.send('Com a quantidade de dinheiro em mãos, você paga o mago! {voltar}')
                        partida['inventario'].add('poção_de_cura')
                if partida['estado'] ==18.2:
                    await msg.channel.send('Você pega a bomba de fumaça e vai até o mago para pagar')
                    if partida['ouro'] <= 39:
                        await msg.channel.send('Você não tem peças de ouro suficientes para comprar esse item!')
                        partida['estado'] = 18
                    else:
                        await msg.channel.send('Com a quantidade de dinheiro em mãos, você paga o mago! {voltar}')
                        partida['inventario'].add('bomba_de_fumaça')
                if partida['estado'] ==20:
                    await msg.channel.send('Você pega o escudo e vai até o ferreiro para pagar.')
                    if partida['ouro'] <= 44:
                        await msg.channel.send('Você não tem peças de ouro suficientes para comprar esse item!')
                        partida['estado'] = 17
                    else:
                        await msg.channel.send('Com a quantidade de dinheiro em mãos, você paga o ferreiro! {voltar}')
                        partida['inventario'].add('escudo_seminovo')
                if partida['estado']==21:
                    await msg.channel.send(inventario_do_jogador)
                    partida['estado']=16
                if partida['estado'] ==23:
                    await msg.channel.send('Depois de uma grande caminhada por essa floresta, você começa a escutar vozes e é parado por três jacares que saíram em um rio próximo e estão estranhamente coordenados. De longe, você vê uma bruxa que parece estar controlando esses animais!')
                
                if partida['vida'] <= 0:
                    await msg.channel.send('Você infelizmente morreu... Vamos voltar do começo!')
                    partida['estado'] = 0
                if partida['estado'] == 23.1:
                    if hit <= 90:
                        await msg.channel.send('Acertou!')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 20 de vida! {Atacar/fugir}')
                        partida['estado'] = 23
                if partida['estado'] ==23.2:
                    if escapar <= 95:
                        await msg.channel.send('Conseguiu escapar! {avançar}')
                        partida['estado'] = 24
                    else:
                        await msg.channel.send('Não escapou')
                        partida['estado'] = 23
                if partida['estado'] ==23.4:
                    if escapar <= 95:
                        await msg.channel.send('Conseguiu escapar! {avançar}')
                        partida['estado'] = 24
                    else:
                        await msg.channel.send('Não escapou')
                        partida['estado'] = 23.1
                if partida['estado'] ==23.6:
                    if escapar <= 95:
                        await msg.channel.send('Conseguiu escapar! {avançar}')
                        partida['estado'] = 24
                    else:
                        await msg.channel.send('Não escapou')
                        partida['estado'] = 23.3
                if partida['estado'] == 23.3:
                    if hit <= 85:
                        await msg.channel.send('Acertou!')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 30 de vida! {Atacar/fugir}')
                        partida['estado'] = 23.1
                if partida['estado'] == 23.5:
                    if hit <= 85:
                        await msg.channel.send('Acertou!')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 30 de vida! {Atacar/fugir}')
                        partida['estado'] = 23.3
                if partida['estado'] == 23.8 or partida['estado'] == 23.7:
                    partida['inventario'].add('couro_de_jacaré')
                    partida['inventario'].add('couro_de_jacaré')
                    partida['inventario'].add('couro_de_jacaré')
                if partida['estado'] == 24.1:
                    if hit <= 85:
                        await msg.channel.send('Acertou!')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 30 de vida! {Atacar/fugir}')
                        partida['estado'] = 24
                if partida['estado'] ==24.2:
                    if escapar <= 95:
                        await msg.channel.send('Conseguiu escapar! {avançar}')
                        partida['estado'] = 26
                    else:
                        await msg.channel.send('Não escapou')
                        partida['estado'] = 24
                if partida['estado'] == 24.3:
                    if hit <= 85:
                        await msg.channel.send('Acertou!')
                    else:
                        await msg.channel.send('Errou')
                        await msg.channel.send('Você recebe mais um ataque do inimigo, perdendo 30 de vida! {Atacar/fugir}')
                        partida['estado'] = 24.1
                if partida['estado'] ==24.4:
                    if escapar <= 95:
                        await msg.channel.send('Conseguiu escapar! {avançar}')
                        partida['estado'] = 24.1
                    else:
                        await msg.channel.send('Não escapou')
                        partida['estado'] = 26
                await msg.channel.send(choice(estados[value]['frases']))
            else:
                await msg.channel.send(frases['inventario_insuficiente'])
            return
    if partida['estado'] == 0:
        await msg.channel.send(choice(estado_do_jogador['frases']))
    else:
        await msg.channel.send(frases['erro'])
bot.run(getenv('DISCORD_TOKEN'))