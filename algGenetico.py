from dataStructures import jogadores, esquemaTatico, Jogador, subList, positionList, getPositionNumber
from BasicOperations import avalia, solucaoInicial
from random import shuffle, randint
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

#Modifica a lista com base na escolha de um grupo de jogadores da mesma posição
#que devem ser trocados aleatóriamente por jogadores da mesma posição
def cruzamento(solucao: List[Jogador]):
    sol = solucao.copy();
    nova_sol = []
    # corte = randint(0, len(jogadores) - 1)
    corte = randint(0, 3) #position from esquema tático
    j = 0

    #Pega uma subList ada posição que foi escolhia para o corte
    pos_list = positionList(corte)

    for i in range(0, len(sol)):

        #Está com a mesma posicao
        if sol[i].posicao == esquemaTatico[corte][0]:
            rand_sus = randint(0, len(pos_list))
            sol[i] = pos_list[rand_sus]

    return nova_sol

def mutacao(solucao: List[Jogador]):
    sol = solucao.copy()
    r = randint(0, len(sol))
    r_palyer = sol[r]
    r_player_pos = r_palyer.posicao

    sub_list = positionList(getPositionNumber(r_player_pos))

    for i in range(0, len(sol) - 1):
        if sol[i][0] == r_player_pos:
            r2 = randint(0, len(sub_list))
            sol[i] = sub_list[r2]
            break

    return sol

    print('unimplemented')

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