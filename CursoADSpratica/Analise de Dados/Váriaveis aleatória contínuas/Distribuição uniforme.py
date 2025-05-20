"""Podem assumir qualquer valor em um intervalo
na pode ter probabilidade exata 0"""
from numpy import size

"""Distribuição simples, tem valores de probabilidades constantes, ou seja sempre iguais
dado nao viciado ==  1 -- 6 todos com 1/6 de probabilidade
"""
"""Parametros
n = quantidade de numeros a serem simulados
min = minimo dos dados
max = maximo dos dados"""

import numpy as np

#Gerar uma distribuiçao uniforme entre 0 e 1 com numpy
uniform_dist = np.random.uniform(0, 1, size = 1000)

#exibir os primeiros 10 valores da distribuição
print(uniform_dist[:10])

"""simulando 10 numeros entre 0 e 1, com um distribuição aleatorio"""

"""Suponha que u dado seja jogado repetidamente, e o resultado de cada jogada seja um numero int entre 1 e 6
com probabilidades iguais para cada resultado, neste caso podemos modelar a dristribuição dos resultados como 
uma diostribuição uniforme discreta"""

#gerar 1000 resultados de um dado
uniform_destr = np.random.randint(1, 7, size = 1000)

#exibir os primeiros 10 valores da distribuição
print(uniform_destr[:10])
