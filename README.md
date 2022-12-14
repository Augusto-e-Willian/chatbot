# chatbot

Um guerreiro, que tem que enfrentar vários inimigos para conseguir chegar no seu destino. Para isso, o jogo vai ser feito de forma com que os inimigos, armas e as outras coisas do jogo são aleatórios de acordo com a parte em que o jogador está no jogo. Para fazer esse sistema de aleatorização, vamos fazer vários modelos de inimigos e armas, que terão propriedades diferentes.

## premissa

Premissa: Jogo RPG rogue-like de ação, onde cada "run" seria diferente, fazendo com que o jogo possa ser "zerado" várias vezes.

### Referências:

Referências: Pokemon e undertale na parte do combate, e Dead Cells na parte do estilo de jogo (rogue-like)

#### Aplicação ideal:

História: O jogo se passa na época da idade média com elementos de fantasia, portanto existem vilarejos com ferreiros, magos, aldeões e tavernas pelo reino. O nosso personagem é um ajudante de ferreiro, que por ter nascido de origem camponesa, nunca conseguiu provar seu valor, porém com a princesa raptada por um feiticeiro poderoso que tem certo controle pelas criaturas e animais do reino, e assim, nosso personagem percebe isso como uma oportunidade de provar seu valor e sair da pobridão, então ele faz uma arma mal feita por não ter muita habilidade com a forja, e sai para a aventura, em busca pra princesa. No meio do caminho, ele vai enfrentar diversos inimigos controlados pelo feiticeiro, e passar por vilas, onde ele vai conseguir se recuperar e comprar itens mais fortes para o resto da sua jornada. No meio dessa jornada, o personagem vai ter que passar por 3 biomas, floresta, deserto e atravessar por nevascas, cada um deles com o seu boss, além de, chegando no final da jornada, para o personagem conseguir entrar na ilha onde está o feiticeiro e a princesa, ele vai precisar passar pelo mar, onde também terão inimigos, como o kraken, e as vilas se tornaram faróis, que terão a mesma serventia das vilas. Chegando na ilha, para conseguir chegar no feiticeiro, o personagem precisará enfrentar 2 generais do feiticeiro, para então lutar contra esse feiticeiro e resgatar a princesa.

Jogabilidade: O personagem começara com uma arma aleatória que vai dar muito pouco dano, elas vao variar entre espada, machado e cajado, além de começar também com um escudo, que negará alguma quantidade do dano. Começando a jornada, o personagem vai iniciar na floresta, enfrentando 3 inimigos (um de cada vez), e então tendo opções, são elas, ir para a floresta densa, onde vai ter inimigos mais fortes, mas que vão dropar mais dinheiro, ir no bosque, onde terão inimigos mais fracos, mas que droparão menos dinheiro, e também terá a opção de formar um acampamento (se tiver o item "tenda"), onde o personagem poderá recuperar a sua vida, para então escolher o seu caminho. O personagem então vai enfrentar mais 3 inimigos, e depois disso, vai chegar em um vilarejo. Nesse vilarejo, terão 2 lojas, a forja, onde terá o ferreiro, que venderá armas, escudos, armaduras pesadas e melhorar a arma, cada uma dessas opções custando dinheiro, a segunda loja será a cabana do mago, onde o mago venderá poções de cura, mana e sorte (Explicada abaixo), além de cajados mágicos. Depois disso, o jogador vai enfrentar os inimigos de novo, mas no lugar do sexto inimigo, terá o boss, a arvore enfeitiçada, e depois disso ele vai para o bioma de deserto. No próximo bioma, a mecânica se manterá a mesma, com inimigos caracteristicos, mais dificeis e uma múmia como o boss final, e depois de matar o boss, o personagem vai para o ambiente de nevasca, que também se manterá o mesmo, com inimigos ainda mais dificeis e um Yeti como o boss. Chegando no final desse bioma, o personagem vai chegar em um vilarejo na beira do mar, que terá um barco a venda para o personagem conseguir comprar e navegar até a ilha do feiticeiro, e se não tiver dinheiro suficiente, tera que voltar os ultimos 3 inimigos para "farmar" dinheiro. No mar, a mecânica de inimigos se manterá a mesma, somente com a mudança dos vilarejos pelos faróis, que terão as mesmas funções do vilarejo, com o boss sendo o Kraken. Derrotando esses inimigos, chegará na ilha do feiticeiro, onde terá que enfrentar 2 mini-bosses (generais) e o feiticeiro como boss final.

Mecânicas:
-Peso: Cada arma, poção e armadura vai ter seu próprio peso, e o personagem não poderá carregar mais que o máximo estipulado (50 de peso base)

-Taxa de acerto: Servira para balanciar o dano das armas leves e pesadas. Como a arma leve terá um dano menor, terá a taxa de acerto de 90%, e as armas pesadas de 70%. A poção de sorte servirá para aumentar essa porcentagem em 10%, além de aumentar o dinheiro dropado pelos monstros em 20%, esse efeito vai durar até a luta de 3 monstros.

-Upgrades: A cada run, quando o personagem morrer, vai "correr" e ganhar experiência, que vai ter a sua quantidade dependendo do progresso feito pelo jogador, que servirá para fazer upgrades

  -Aumento de vida: ganha 10 de vida (Começando com 100)
  
  -Aumento de ataque em armas leves: ganha 5 de ataque
 
  -Aumento de ataque em armas pesadas: ganha 10 de dano
  
  -Aumento de sorte: ganha 2% de taxa de acerto, e mais 15% de dinheiro
  
  -Aumento de mana: ganha 5 de mana total
  
  -Aumento de peso: ganha 5 de peso total
  
  -Melhores ferreiros e magos: São vendidas melhores armas e poções nas lojas

-Poções e armas:
 
 -Poções:
    
    -Poção de vida: Recupera 50% da vida (+70% se tiver o upgrade "Melhores ferreiros e magos")
    
    -Poção de mana: Recupera 50% da mana (+70% se tiver o upgrade "Melhores ferreiros e magos")
    
    -Poção de sorte: Aumenta 10% de taxa de acerto, e os inimigos dropam 20% a mais de dinheiro (15%, 25% se tiver o upgrade "Melhores ferreiros e magos")
    
    -Poção de fraqueza: Diminui 20% do dano do inimigo (arremessável)
    
    -Poção de envenenamento: Atribui um dano passivo no inimigo de 5 (arremessável)

 -Armas:
    
    -Espada: "neutro", não tem benefícios, mas tem um dano decente. 90% de chance de acerto
    
    -Adaga: Dano reduzido, mas tem chance de causar sangramento nos inimigos. 90% de chance de acerto
    
    -Cajado: Gasta mana para ser utilizado, mas tem 100% de chance de acerto.
    
    -Machado: Dano aumentado, mas possui 70% de chance de acerto.

-Mana: Utilizada para usar o cajado. (100 de mana base)

-Vida: Terá seu maximo aumentado através de upgrades no começo de uma nova run. (100 de vida base)

-Armadura: Está no escudo/armadura e nega uma de dano.