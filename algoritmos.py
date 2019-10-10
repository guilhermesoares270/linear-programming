from BasicOperations import solucaoInicial, avalia, shemaTransverse, sucessores, subList, positionList
from dataStructures import jogadores, esquemaTatico, Jogador, positions
from typing import Callable, List
from random import randint

def subidaDeEncosta():
    atual = solucaoInicial(jogadores, esquemaTatico)
    va = avalia(atual)
    # print('inicial', va)

    while (True):
        #Escolhe uma posição para gerar os sucessores
        pos = randint(0, 3)

        #Gerar uma sublista a partir da lista de todos os jogadores
        #Contendo apenas os jogadores da posição escolhida
        poslist = positionList(pos)

        #Cada posição pode ter mais de um jogador associado
        #Ex: zagueiro 4 no time
        #Por isso deve-se escolher, de forma aleatória, um dos 4 que deve ser substituido pelo sucessores
        PlayerTeamPosition(positions[pos], esquemaTatico)

        #Gerar os sucessores para aquela posição e devolve o que tiver o melhor resultado
        #quando submetido a função avalia
        prox = sucessores(poslist, atual, pos)

        #Avalia o sucessor escolhido
        vp = avalia(prox)
        # print('avalia prox', vp)

        if vp < va:
            va = vp
        else:
            break

    return va

def subidaDeEncosta2():
    t_max = 10
    tentativas = 0
    atual = solucaoInicial(jogadores, esquemaTatico)
    va = avalia(atual)

    while (True):
        #Escolhe uma posição para gerar os sucessores
        pos = randint(0, 3)

        #Gerar uma sublista a partir da lista de todos os jogadores
        #Contendo apenas os jogadores da posição escolhida
        poslist = positionList(pos)

        #Cada posição pode ter mais de um jogador associado
        #Ex: zagueiro 4 no time
        #Por isso deve-se escolher, de forma aleatória, um dos 4 que deve ser substituido pelo sucessores
        PlayerTeamPosition(positions[pos], esquemaTatico)

        #Gerar os sucessores para aquela posição e devolve o que tiver o melhor resultado
        #quando submetido a função avalia
        prox = sucessores(poslist, atual, pos)

        #Avalia o sucessor escolhido
        vp = avalia(prox)

        if vp >= va:
            if tentativas > t_max:
                return va
            else:
                tentativas += 1
        else:
            atual = prox
            va = vp
            tentativas = 0
    return va

#This function should choose a random player from a position
#and return his posion in the atual list
#example [1, 2 , 3, 4, 5 , 6 , 7, 8 , 9 ,10, 11]
#choose random zagueiro theres 4 in the team
#ans the team has halways the same compositon goleiro, zagueiros, meias, atacantes
def PlayerTeamPosition(position: str, esquemaTatico: esquemaTatico):
    # print('position', position)
    iniPos = 0
    rpos = 0
    for x in esquemaTatico:
        # print('iniPos', iniPos, 'esquemaValue', x[1])
        if x[0] == position:
            # print('positionFind', x[0])
            # print('position Range', iniPos, iniPos + x[1])
            rpos = randint(iniPos, iniPos + x[1])
            break
        iniPos += x[1]
    # print('random position', rpos)
    return rpos

# def postionMap(posindex: int):
    

# creates a sublist of a given position
def subList(pos: str, jogadores: List[Jogador])-> List[Jogador]:
    res: List[Jogador] = []
    for jogador in jogadores:
        if jogador.posicao == pos:
            res.append(jogador)
    return res

res = subidaDeEncosta()
res2 = subidaDeEncosta2()
print('subida de encosta', res)
print('subida de encosta alternativo', res2)