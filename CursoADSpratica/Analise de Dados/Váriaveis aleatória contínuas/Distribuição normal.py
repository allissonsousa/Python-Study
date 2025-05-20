"""Se vc nao usar media e desvio o python vai entender q sao 0 e 1
A forma dessa distribuição é um sino quando em grafico"""
from PIL.ImageOps import scale

"""Suponde q um analista financeiro quer saber a chace de obter um retorno 10k em um mes
a media sendo 8 mil, com desvio padrao de 2k
qual a chance do retorno ser maior q 10k
"""

from scipy.stats import norm

#media e desvio padrao

mu = 8
sigma = 2

#definir o valor minimo de retorno desejado
retorno_minimo = 10

#calcular a probabilidade com scipy.stats
probabilidade = 1 - norm.cdf(retorno_minimo, loc = mu, scale = sigma)

print(f"A probabilidade de ter um retorno superior a {retorno_minimo} reais é de {probabilidade :.2f}")