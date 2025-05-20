"""Se vc nao usar media e desvio o python vai entender q sao 0 e 1
A forma dessa distribuição é um sino quando em grafico"""
from PIL.ImageOps import scale

"""Suponde q um analista financeiro quer saber a chace de obter um retorno 10k em um mes
a media sendo 8 mil, com desvio padrao de 2k
qual a chance do retorno ser maior q 10k
"""

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

#media e desvio padrao

mu = 8
sigma = 2

#definir o valor minimo de retorno desejado
retorno_minimo = 10

#calcular a probabilidade com scipy.stats
probabilidade = 1 - norm.cdf(retorno_minimo, loc = mu, scale = sigma)

print(f"A probabilidade de ter um retorno superior a {retorno_minimo} reais é de {probabilidade :.2f}")

"""Para fazer um grafico pode se usar a função norm.pdf para funcao de densidade de probabilidade
"""
#------------------------------------
"""Vamos criar um grafico da distribuição normal para a altura de pessoas adultar com media 170cm e desvio padrao 10
usando pdf e plt
"""
media = 170
desvio_padrao = 10

# intervalo de alturas para o calculo de densidade de probabilidade
alturas = np.linspace(media - 4 * desvio_padrao, media + 4 * desvio_padrao, 1000)

#calculo da densidade de probabilidade usando norm.pdf
densidade_probabilidade = norm.pdf(alturas, loc=media, scale=desvio_padrao)

#grafico
plt.plot(alturas, densidade_probabilidade)
plt.xlabel('Altura (cm)')
plt.ylabel('Densidade de probabilidade')
plt.title('Distribuição normal para a altura de pessoas adultas')
plt.grid(True)
plt.show()
