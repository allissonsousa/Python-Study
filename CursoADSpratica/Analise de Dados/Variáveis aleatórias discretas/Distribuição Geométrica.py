"""Descreve a probabilidade dentro de uma sequencia de bernoulli em uma sequencia de tentativas
 até q se obtenha o primeiro sucesso
 ex: jogar uma moeda até q caia cara
 ex: jogar uma bola de basquete até o acerto
 ex: retirar uma bola de um saco com bolas azuis e verdes
 qual a chance de tirar uma bola azul primeiro, ou qual a probabiliade de se obter uma bola verde
 só na terceira vez

"""
# k = tentativas até o sucesso
# x = numero de fracassos
# p = probabilidade de sucesso

import scipy.stats as stats

#Definir a probabiliadade de sucesso (p)
p = 0.3

#Definir o número dde tentativas até o primiro sucesso(k)
k = 5

#Calcular a probabilidade de x=k usando a funçao pmf da distribuição geométrica
probabilidade = stats.geom.pmf(k,p)

print(f"A probabiliade dde precisar dde exatamente {k} dardos é de {probabilidade :.2f}")
