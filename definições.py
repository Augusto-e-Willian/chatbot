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
        'frases': ['Você encontrou um monstro no caminho e foi atacado, perdendo 25 pontos de vida! {Atacar/fugir}'],
        'vida': -25,
        'proximos_estados': {
            '[aA]taca(r)': 2,
            '[fF]ugi(r)': 3
        },
        'inventario': {}
    },
    2: {
        'frases': [''],
        'vida': 0,
        'proximos_estados': {
            '[aA]vançar': 4,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    3: {
        'frases': ['Bomba de fumaça usada para tentar escapar!'],
        'vida': 0,
        'proximos_estados': {
            '[rR]einiciar?': 0
        },
        'inventario': {'bomba_de_fumaça'}
    },
    4: {
        'frases': ['Uma espada apareceu: O=|======> / Pegar? {sim/não}'],
        'vida': 0,
        'proximos_estados': {
            '[sS](i)+m': 5,
            '[nN][aã]+o': 5,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    5: {
        'frases': ['Você pegou a espada! {Continuar/descansar}'],
        'vida': 0,
        'proximos_estados': {
            '[cC]ontinua+r': 6,
            '[dD]escan[sc]a+r': 7,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    7: {
        'frases': ['Você usou uma poção de cura, recuperando 50 pontos de vida! {continuar}'],
        'vida': 50,
        'proximos_estados': {
            '[cC]ontinua+r': 6,
            '[rR]einiciar?': 0
        },
        'inventario': {'poção_de_cura'}
    }, 
    6: {
        'frases': ['Uma caveira de carater duvidoso aparece, não parecendo causar ameaça e liberando o caminho para sua passagem. Você escolhe matar a caveira a sangue frio ou passar de forma pacifica? {passar/atacar}'],
        'vida': 0,
        'proximos_estados': {
            '[aA]taca+r': 8,
            '[pP]assa+r': 9,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    8: {
        'frases': ['Você ataca o ser indefeso, vendo o quão desapontado ele está com você. Parabéns monstro, você recuperou uma "espada generica" dos restos do pobre coitado! {Continuar}'],
        'vida': 0,
        'proximos_estados': {
            '[cC]ontinua+r': 10,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    9: {
        'frases': ['Você realmente acreditou na inocência de uma caveira perambulando por uma floresta densa? Assim que você da as costas para a caveira, ela tira o próprio fêmur, atingindo você na cabeça! Você sai correndo dela. -50 de vida. {continuar}'],
        'vida': -50,
        'proximos_estados': {
            '[cC]ontinua+r': 11,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    }
}


partidas = {}