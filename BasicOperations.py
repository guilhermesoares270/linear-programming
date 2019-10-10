from dataStructures import jogadores, esquemaTatico, Jogador
from typing import Callable, List
from random import randint
from pprint import pprint

def solucaoInicial(jogadores, esquemaTatico):
    searchFor = [x[1] for x in esquemaTatico]

    goleiros = shemaTransverse('goleiro', 1, jogadores, printTest)
    zagueiro = shemaTransverse('zagueiro', 4, jogadores, printTest)
    meia = shemaTransverse('meia', 3, jogadores, printTest)
    atacante = shemaTransverse('atacante', 3, jogadores, printTest)

    res = []
    res.extend(goleiros)
    res.extend(zagueiro)
    res.extend(meia)
    res.extend(atacante)

    return res

def printTest(quantidade: int, posicao: str, jogador: Jogador):
    print(posicao, jogador.valor)

# atual lista inicial de jogadores escolhidos (solução inicial)

#Deve gerar vários e devolver o melhor
# def sucessores(positionList: List[int], atual: List[int], posAtual: int):

"""Generates a list of
"""
def sucessores(positionList: List[Jogador], atual: List[Jogador], posAtual: int):

    atualList = atual.copy()
    sucessores = []

    for jogador in positionList:
        atualList[posAtual] = jogador
        
        sucessores.append(atualList.copy())
        atualList = atual.copy()
    
    # for sus in sucessores:
    #     print(avalia(sus))

    current = atual
    for sus in sucessores:
        if avalia(sus) < avalia(current):
            current = sus

    # print('sucessores')
    # print(avalia(current))
    # print('')
    return current

# goleiros = subList('goleiro', jogadores)
# zagueiros = subList('zagueiro', jogadores)
# meias = subList('meia', jogadores)
# atacantes = subList('atacante', jogadores)

# Creates a sublist of a given position
# This is usefull for separing the positions
def subList(pos: str, jogadores: List[Jogador])-> List[Jogador]:
    res: List[Jogador] = []
    for jogador in jogadores:
        if jogador.posicao == pos:
            res.append(jogador)
    return res

def positionList(pos = 0)-> List[Jogador]:
    if pos == 0:
        return subList('goleiro', jogadores)
    elif pos == 1:
        return subList('zagueiro', jogadores)
    elif pos == 2:
        return subList('meia', jogadores)
    elif pos == 3:
        return subList('atacante', jogadores)
    else:
        return subList('goleiro', jogadores)

#Escolhe um jogador de uma lista de jogadores
def shemaTransverse(
        posicao,
        quantidade,
        jogadores,
        closure: Callable[[int, str, Jogador], List[int]]
    ):
    s1 = []
    counter = 0
    for jogador in jogadores:

        if quantidade <= 0:
            break

        if jogador.posicao == posicao:
            # s1.append(jogador.valor)
            s1.append(jogador)
            quantidade -= 1
        
            # closure(quantidade, jogador.posicao, jogador)

    return s1

# def choosePlayers(
#         quantidade: int,
#         posicao: str,
#         jogador: Jogador,
#     )-> List[int]:

#     res = []

#     if quantidade <= 0:
#         return []

#     if jogador.posicao == posicao:
#         res.append(jogador.valor)
#         quantidade -= 1

#     return res

def avalia(solucao: List[Jogador]):
    res = 0
    for sol in solucao:
        res += sol.valor
    return res