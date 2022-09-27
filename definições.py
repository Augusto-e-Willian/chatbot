# Dicionário com as definições da máquina de estados do jogo.
# As opções dos jogadores são definidas como expressões regulares.
from random import randint

estados = {
    0: {
        'frases': ['Digite "#começar" para iniciar o jogo.'],
        'proximos_estados': {
            '#[Cc]omeça(r)': 1
        }
    },
    1: {
        'frases': ['Um monstro apareceu!', 'Você deu de cara com um monstro!'],
        'proximos_estados': {
            '#[aA]+tacar': 2,
            '#[fF]+ugir': 3
        }
    },
    2: {
        'frases': [hit],
        'proximos_estados': {
            '#[rR]einicia(r)': 1
        }
    },
    3: {
        'frases': [escape],
        'proximos_estados': {
            '#[rR]einicia(r)': 1
        }
    }
}

# Dicionário com os estados correntes de cada jogador.
partidas = {}