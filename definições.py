frases = {
    'inventario_insuficiente': 'Sem os recursos necessários para avançar.',
    'erro': 'I\'m sorry Dave, I\'m afraid I can\'t do that.'
}

estados = {
    0: {
        'frases': ['Digite "iniciar" para começar o jogo.'],
        'vida': 100,
        'proximos_estados': {
            '[iI]niciar?': 1
        },
        'inventario': {}
    },
    1: {
        'frases': ['--------------'],
        'vida': -25,
        'proximos_estados': {
            '[aA]taca(r)': 2,
            '[fF]ugi(r)': 3
        },
        'inventario': {}
    },
    2: {
        'frases': ['-------------------------'],
        'vida': 5,
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
            '[sS](i)+m': 5,
            '[nN][aã]+o': 5
        },
        'inventario': {}
    },
    5: {
        'frases': ['Você pegou a espada! / Continuar ou descansar?'],
        'proximos_estados': {
            '[cC]ontinua+r': 6,
            '[dD]escan[sc]a+r': 7
        },
        'inventario': {}
    },
    6: {
        'frases': ['Você usou uma poção de cura, recuperando 50 pontos de vida!'],
        'vida': 234234,
        'proximos_estados': {
            '[cC]ontinua+r': 8
        },
    },  'inventario': {'poção_de_cura'}
}


partidas = {}