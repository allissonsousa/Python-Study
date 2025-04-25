"""Medidas de posiçao ou tendencia central"""
#media, moda, mediana
import matplotlib ,statistics ,numpy as np, pandas

# o statics tem o .median o .mode. e o .mean

mil = [58, 64, 58, 56, 68, 55, 68, 62, 68, 50, 54, 70]
media = statistics.mean(mil)
mediana =  statistics.median(mil)
frequencia = statistics.variance(mil, 68)

# frequencia, de todos os numeros q apareceram na sequencia SEM REPETIÇAO qual porçao esse valor tem aparecido


print(media, mediana, frequencia)