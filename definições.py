frases = {
    'inventario_insuficiente': 'Sem os recursos necessários para avançar.',
    'erro': 'I\'m sorry Dave, I\'m afraid I can\'t do that.'
}

estados = {
    0: {
        'frases': ['Digite "iniciar" para começar o jogo.'],
        'vida': 100,
        'ouro': 10,
        'proximos_estados': {
            '[iI]niciar?': 1
        },
        'inventario': {}
    },
    1: {
        'frases': ['Você encontrou um monstro no caminho e foi atacado, perdendo 20 pontos de vida! {atacar/fugir}'],
        'vida': -20,
        'ouro': 0,
        'proximos_estados': {
            '[aA]taca(r)': 2,
            '[fF]ugi(r)': 3
        },
        'inventario': {}
    },
    2: {
        'frases': [''],
        'vida': 0,
        'ouro': 15,
        'proximos_estados': {
            '[aA]vançar': 4,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    3: {
        'frases': ['Bomba de fumaça usada para tentar escapar!'],
        'vida': 0,
        'ouro': 0,
        'proximos_estados': {
            '[rR]einiciar?': 0
        },
        'inventario': {'bomba_de_fumaça'}
    },
    4: {
        'frases': ['Uma espada apareceu: O=|======> / Pegar? {sim/não}'],
        'vida': 0,
        'ouro': 0,
        'proximos_estados': {
            '[sS](i)+m': 5,
            '[nN][aã]+o': 4.5,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    4.5: {
        'frases': ['Você deixa a espada de lado, e agora você pode continuar sua jornada ou usar uma poção de cura para recuperar 50 pontos de vida {continuar/descansar}'],
        'vida': 0,
        'ouro': 0,
        'proximos_estados': {
            '[cC]ontinua+r': 6,
            '[dD]escan[sc]a+r': 7,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    5: {
        'frases': ['Você pegou a espada!, agora você pode continuar sua jornada ou usar uma poção de cura para recuperar 50 pontos de vida {continuar/descansar}'],
        'vida': 0,
        'ouro':0,
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
        'ouro': 0,
        'proximos_estados': {
            '[cC]ontinua+r': 6,
            '[rR]einiciar?': 0
        },
        'inventario': {'poção_de_cura'}
    }, 
    6: {
        'frases': ['Uma caveira de carater duvidoso aparece, não parecendo causar ameaça e liberando o caminho para sua passagem. Você escolhe matar a caveira a sangue frio ou passar de forma pacifica? {passar/atacar}'],
        'vida': 0,
        'ouro': 0,
        'proximos_estados': {
            '[aA]taca+r': 8,
            '[pP]assa+r': 9,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    8: {
        'frases': ['Você ataca o ser indefeso, vendo o quão desapontado ele está com você. Parabéns monstro, você recuperou uma "espada generica", junto com 20 peças de ouro dos restos do pobre coitado! {continuar}'],
        'vida': 0,
        'ouro': 20,
        'proximos_estados': {
            '[cC]ontinua+r': 10,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    9: {
        'frases': ['Você realmente acreditou na inocência de uma caveira perambulando por uma floresta densa? Assim que você da as costas para a caveira, ela tira o próprio fêmur, atingindo você na cabeça! Você sai correndo dela. -50 de vida. {continuar}'],
        'vida': -50,
        'ouro': 0,
        'proximos_estados': {
            '[cC]ontinua+r': 10,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    10: {
        'frases': ['Passando por um pântano, da lama algo te puxa, um ser que parece vir de outro mundo, com um corpo lamacento e humanoide, esse não parece um inimigo que vai ser facilmente derrotado. - 30 de vida / {atacar/fugir}'],
        'vida': -30,
        'ouro': 0,
        'proximos_estados': {
            '[aA]tacar': 12,
            '[fF]ugir': 13,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    12: {
        'frases': ['Mesmo cortando o inimigo de ponta a ponta, ele não morre, porém é visível que está mais fraco que antes. {atacar/fugir}'],
        'vida': -10,
        'ouro': 0,
        'proximos_estados': {
            '[aA]taca+r': 14,
            '[fF]ugi+r': 13,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    13: {
        'frases': ['Bomba de fumaça usada para tentar escapar!'],
        'vida': 0,
        'ouro': 0,
        'proximos_estados': {
            '[rR]einiciar?': 0
        },
        'inventario': {'bomba_de_fumaça'}
    },
    14: {
        'frases' : ['A luta finalmente termina, e você então pega 30 peças de ouro do corpo lamacento... O que um montro assim faria com ouro? E você tem a chance de descansar! {continuar}'],
        'vida': 0,
        'ouro': 30,
        'proximos_estados': {
            '[cC]ontinua+r': 15,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    15: {
        'frases': ['Da distância, você consegue ver um vilarejo {ir/ignorar}'],
        'vida': 0,
        'ouro': 0,
        'proximos_estados': {
            '[iI]+r': 16,
            '[iI]gnora+r': 10000,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    16: {
        'frases': ['Entrando no vilarejo, você consegue ver a ferraria do ferreiro, e a loja de poções do mago, além da taverna que parece um bom lugar para descansar. Quando achar que está pronto, pode continuar sua aventura! {ferreiro/mago/taverna/inventario/continuar}'],
        'vida': 0,
        'ouro': 0,
        'proximos_estados': {
            '[cC]ontinua+r': 22,
            '[iI]nvent[aá]ri+o': 21,
            '[fF]erreiro':  17,
            '[mM]ago': 18,
            '[tT]averna': 19,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    17: {
        'frases': [''],
        'vida': 0,
        'ouro': 0,
        'proximos_estados': {
            '[cC]ompra+r': 20,
            '[vV]olta+r': 16,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    18: {
        'frases': [''],
        'vida': 0,
        'ouro': 0,
        'proximos_estados': {
            '[vV]id+a': 18.1,
            '[fF]uma[cç]+a': 18.2,
            '[vV]olta+r': 16
        },
        'inventario': {}
    },
    18.1: {
        'frases': [''],
        'vida': 0,
        'ouro': -20,
        'proximos_estados': {
            '[vV]olta+r': 16,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    18.2: {
        'frases': [''],
        'vida': 0,
        'ouro': -40,
        'proximos_estados': {
            '[vV]olta+r': 16,
            '[rR]einicia+r': 0
        },
        'inventario': {}
    },
    19: {
        'frases': ['Você passa um tempo na taverna bebendo e descansando, e se sente totalmente recuperado! {voltar}'],
        'vida': 100,
        'ouro': 0,
        'proximos_estados': {
            '[vV]olta+r': 16,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    20: {
        'frases': [''],
        'vida': 0,
        'ouro': -45,
        'proximos_estados': {
            '[vV]olta+r': 16,
            '[rR]einiciar?': 0
        },
        'inventario': {}
    },
    21: {
        'frases': [''],
        'vida': 0,
        'ouro': 0,
        'proximos_estados': {
            'skfsdkfopskpfo': 11011101010
        },
        'inventario': {}
    },
    22: {
        'frases': ['Saindo do vilarejo, você anda por um longo caminho até chegar em uma floresta completamente fechada, onde a luz mal consegue entrar.'],
        'vida': 0,
        'ouro': 0,
        'proximos_estados':{
            '[cC]ontinua+r': 23
        },
        'inventario': {}
    },
    23: {
        'frases': ['Os jacarés te atacam, causando 20 de dano! {atacar/fugir}'],
        'vida': -20,
        'ouro': 0,
        'proximos_estados': {
            '[aA]taca+r': 23.1,
            '[fF]ugi+r': 23.2
        },
        'inventario': {}
    },
    23.1: {
        'frases': ['Você consegue matar um dos jacarés, mas ainda faltam mais 2, que te causam 15 de dano! {atacar/fugir}'],
        'vida': -15,
        'ouro': 0,
        'proximos_estados': {
            '[aA]taca+r': 23.3,
            '[fF]ugi+r': 23.4
        },
        'inventario': {}
    },
    23.3: {
        'frases': ['Com os dois jacarés derrotados, agora só falta mais um! {atacar/fugir}'],
        'vida': -10,
        'ouro': 0,
        'proximos_estados': {
            '[aA]taca+r': 23.5,
            '[fF]ugi+r': 23.6
        },
        'inventario': {}
    },
    23.5: {
        'frases': ['Você finalmente consegue derrotar os animais e vai em direção a bruxa, que parece estar muito assustada. Chegando nela, a bruxa te pede piedade e te promete dar um saco com peças de ouro além de te ajudar com suas feridas. {atacar/desculpar'],
        'vida': 0,
        'ouro': 0,
        'proximos_estados': {
            '[aA]taca+r': 23.7,
            '[dD]esculpa+r': 23.8
        }
    }
}


partidas = {}