"""Diferente do bernoulli q só tem como ter dois resultados, a binomial tem 2 paramentros, que é o numero de tentativas
e a probabilidade de sucesso em cada lançamento"""

"""Uma moeda lançada 3x, qual a probabilidade de se obter 2 caras"""

import scipy.stats as stats

# Cria um distribuição binomial com n (tentativas) = 20 e p (probabilidade por tentativa) = 0,2
ditribuicao = stats.binom(20, 0.2)

# Calcular a probabilidade de obret exatamente 3 sucesos
probabilidade_8_sucesso = ditribuicao.pmf(8)   #probabilidade dp X ser igual a 8

# Calcular a probabilidade de obter 8 ou  menos sucessos
probabilidade_8_ou_menos_sucesso = ditribuicao.cdf(8)   #probabilidade do X ser igual ou menor q x

# Clacular a média e a variancia dea distribuição
media =  ditribuicao.mean()
variancia = ditribuicao.var()

# Exibir resultados
print("Probabilidade de obter exatamente 3 sucessos", probabilidade_8_sucesso)
print("Probabilidade de obter 8 ou menos sucessos", probabilidade_8_ou_menos_sucesso)
print("Média:", media)
print(f"Variancia:{variancia :.2f}")
