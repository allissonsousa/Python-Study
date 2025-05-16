"""Numero de elemento sucesso obtidos em uma certa quantidade de tentativas sem reposição, realizadas sobre uma
populaçao de uma certa quantidade de elementos, parte favoraveis e parte nao favoraveis"""
"""os parametros serão:
x = numero de suceso DESEJADO
M = tamanho da população
n = numero total de sucessos na população
k =  tamanho da amostra retirada da população

usando a função : stats.hypergeom(x,m,n,k) se obtem o resultado"""

"""uma empresa deseja avaliar a satisfação dos clientes em relação a um produto. A população de 
clientes é de 100 pessoas e 20% delas são consideradas fiéis. A empresa seleciona aleatoriamente 
uma amostra de 10 clientes para realizar a pesquisa. Qual é a probabilidade de obter exatamente 3 
clientes fiéis na amostra?"""

import scipy.stats as stats

#criar uma ditribuição hipergeométrica com M = 100, N = 20, k = 10
distribuicao = stats.hypergeom(100,20,10)

#Calcular a probabilidade de obter exatamente 3 sucessos na amostra
probabilidade_3_sucessos = distribuicao.pmf(3)

#calcular a probabilidade de obter 3 OU menos sucessos na amostra
probabilidade_3_ou_menos_sucessos = distribuicao.cdf(3)

#calcular a média e a variancia da distribuição
media = distribuicao.mean()
variancia = distribuicao.var()

print("Probabilidade de obter exatamente 3 sucessos na amostra:", probabilidade_3_sucessos)
print("Probabilidade de obter 3 ou menos sucessos na amostra", probabilidade_3_ou_menos_sucessos)
print("Média:", media)
print("Variancia:", variancia)
