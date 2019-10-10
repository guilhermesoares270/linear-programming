import pandas as pd
import BasicOperations as bo
import dataStructures as ds

df = pd.read_csv('2019-medias-jogadores.csv', delimiter=',', usecols=['player_slug', 'status'])
# df = pd.read_csv('2019-medias-jogadores.csv', delimiter=',')

# print(df)

s1 = bo.solucaoInicial(ds.jogadores, ds.esquemaTatico)

print(s1)
