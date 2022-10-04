frases = {
    'inventario_insuficiente': 'Sem os recursos necessários para avançar.',
    'erro': 'I\'m sorry Dave, I\'m afraid I can\'t do that.'
}

estados = {
    0: {
        'frases': ['Digite "iniciar" para começar o jogo.'],
        'proximos_estados': {
            '[iI]niciar?': 1
        }
    },
    1: {
        'frases': ['Você encontrou um monstro no caminho! Atacar ou fugir?'],
        'proximos_estados': {
            '[aA]taca(r)': 2,
            '[fF]ugi(r)': 3
        },
        'inventario': {}
    },
    2: {
        'frases': [''],
        'proximos_estados': {
            '[aA]vançar': 4,
            '[rR]einiciar?': 1
        },
        'inventario': {}
    },
    3: {
        'frases': ['Bomba de fumaça usada para tentar escapar!'],
        'proximos_estados': {
            '[rR]einiciar?': 1
        },
        'inventario': {'bomba_de_fumaça'}
    },
    4: {
        'frases': ['Uma espada apareceu: O=|======> / Pegar?'],
        'proximos_estados': {
            '[sS](i)+m': 1
        },
        'inventario': {}
    }
}


partidas = {}