from dataStructures import jogadores, esquemaTatico, Jogador
from BasicOperations import avalia, solucaoInicial
from random import shuffle
from typing import List

# Algoritmo genético

def pop_inicial(tam_p):
    l_jogadores = jogadores.copy()
    populacao = []

    for i in range(tam_p):
        shuffle(l_jogadores)
        populacao.append(solucaoInicial(l_jogadores, esquemaTatico))
    
    return populacao

#dist absoluta para relativa
def fitness(solucao: List[Jogador]):
    tp = len(solucao)
    soma = 0
    f = [x for x in range(tp)] #preenche a lista

    for i in range(tp): 
        f[i] = 1/avalia([solucao[i]]) #minimização
        soma += f[i]

    for j in range(tp):
        f[j] = f[1]/soma

    return f

# pop_inicial = pop_inicial(10)
# print(pop_inicial)

# fit = fitness(solucaoInicial(jogadores, esquemaTatico))
# print(fit)
# print('a')

# freq = 0
# for i in range(len(fit)):
#     freq += fit[i]

# print('ava')
# print(freq)