"""Medidas de variabilidades ou dispersão"""
import statistics

import pandas as pd, statistics, numpy
from fontTools.misc.cython import returns

# quao dispersos estão os dados em relação ao valor da media
# variancia, desvio padrão, amplitude, quartil, coeficiencia de variação e desvio médio absoluto
#  statitics.variance
# statitics.stdev --- desvio padrão
# numpy para amplitude .ptp
# quartil numpy.percentile [25,50,75]  25- primeiro quartil, 50 mediana, 75 quartil

# a função describe() retorna as estatisticas dos dados com todas as medidas citadas anteriormente

# ex1
dados = [58,64,58,56,68,62,55,68,68,50,54,70]
print(numpy.mean(dados))
print(numpy.std(dados))
print(numpy.median(dados))
print(statistics.variance(dados, 68))

cota = dados.count(68)
total = len(dados)
cota_rel = cota / total
print(cota_rel.__round__(4))

