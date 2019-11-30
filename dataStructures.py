class Jogador:
    def __init__(self, posicao, valor):
        self.posicao = posicao
        self.valor = valor
    
    def __str__(self):
        return "posicao: " + self.posicao

class Positions:
    GOLEIRO = 7
    ZAGUEIRO = 4
    MEIA = 9
    ATACANTE = 3

jogadores = [
    Jogador('meia', 50),
    
    Jogador('goleiro', 500),
    Jogador('goleiro', 600),
    Jogador('goleiro', 300),

    Jogador('zagueiro', 250),
    Jogador('zagueiro', 100),
    Jogador('zagueiro', 200),
    Jogador('zagueiro', 300),
    Jogador('zagueiro', 400),
    Jogador('zagueiro', 500),

    Jogador('meia', 10),
    Jogador('meia', 20),
    Jogador('meia', 30),
    Jogador('meia', 40),

    Jogador('atacante', 600),
    Jogador('atacante', 700),
    Jogador('atacante', 800),
    Jogador('atacante', 900)
    
    # Jogador(Positions.GOLEIRO, 300),
    # Jogador(Positions.GOLEIRO, 500),
    # Jogador(Positions.GOLEIRO, 600),
    # Jogador(Positions.MEIA, 150)
]

esquemaTatico = [
    ['goleiro', 1],
    ['zagueiro', 4],
    ['meia', 3],
    ['atacante', 3]
]

def getPositionNumber(pos):
    if pos == 'goleiro':
        return 0
    elif pos == 'zagueiro':
        return 1
    elif pos == 'meia':
        return 2
    elif pos == 'atacante':
        return 3
    else:
        return 0

positions = ['goleiro', 'zagueiro', 'meia', 'atacante']