from pokemon import Pokemon, desenho_pokemons, Jogador
from random import randint

player=Jogador()
escolha=int(input("Escolha o seu pokemon: \n1)Charmander\n2)Squirtle\n3)Bulbassauro\n: "))
meu_pokemon=Pokemon(escolha)
for k,v in desenho_pokemons.items():
    if k == meu_pokemon.raca:
        print(v)
        meu_pokemon.escolha_nome()
while True:
    caminho=input(f'Escolha entre ir ao mercado para comprar suprimentos ou batalhar(mercado/batalhar): ')
    while (caminho!="mercado") and (caminho!="batalhar") and (caminho!="pokecenter"):
        caminho=input(f'Escolha entre ir ao mercado para comprar suprimentos ou batalhar(mercado/batalhar): ')
    if caminho=="mercado":
        player.loja()
        continue
    if caminho=="batalhar":
        pokemon_contra=randint(2,3) #################LEMBRAR MUDAR PARA (1,3)
        pokemon_contra=Pokemon(pokemon_contra)
    if caminho=="pokecenter":
        meu_pokemon.pokecenter()
    while (pokemon_contra.vida>0):
        print(f'\nhp: {pokemon_contra.vida}\n\n{pokemon_contra.ascii}\n\n')
        print(f'--------------------------------------------\n Vida de {meu_pokemon.nome}: {meu_pokemon.vida}\n--------------------------------------------\nMoedas:{player.moedas}')
        acao=input(f'-------   -------   -------\n/ATACAR/  /FUGIR/   /ITENS/\n-------   -------   -------\n: ')
        if acao=="itens":
            if len(player.inventario) >0:
                quantidade_de_cura=player.usar_itens()
                meu_pokemon.curar(quantidade_de_cura)
            else:
                print(f'Você não tem itens no seu inventário!')
        if acao=="fugir":
            chance=randint(0,100)
            if chance<=90:
                print("Conseguiu escapar!")
                break
            else:
                print("Não conseguiu escapar")
        if acao =="atacar":
            x=0
            for k,v in meu_pokemon.ataques.items():
                x+=1
                print(f'{x}){k}: {v} dano\n')
            escolha_ataque=int(input("Selecione o número que corresponde ao ataque desejado: "))
            for i in range(len(meu_pokemon.ataques)):
                for k,v in meu_pokemon.ataques.items():
                    if (escolha_ataque==1) and (i==0):
                        dano=v
                        break
                    if (escolha_ataque==2) and (i==1):
                        dano = v
            pokemon_contra.dano(dano,meu_pokemon.tipo,1)
        escolha_ataque_inimigo=randint(0,1)
        for i in range(len(pokemon_contra.ataques)):
                for k,v in pokemon_contra.ataques.items():
                    if (escolha_ataque_inimigo==0) and (i==0):
                        dano=v
                        break
                    if (escolha_ataque_inimigo==1) and (i==1):
                        dano = v
        print(f'\nTurno do inimigo:\n')
        meu_pokemon.dano(dano,pokemon_contra.tipo,pokemon_contra.vida)
        if meu_pokemon.vida<=0:
            print(f'Infelizmente a vida de {meu_pokemon.nome} chegou a 0, o jogo acabou :(')
            exit()
        if pokemon_contra.vida<=0:
            meu_pokemon.ganho_xp(pokemon_contra.nivel)
            meu_pokemon.subida_nivel(escolha)
            player.moedas_vitoria(pokemon_contra.nivel)
            print(f'nivel = {meu_pokemon.nivel} // xp = {meu_pokemon.xp}')
            
