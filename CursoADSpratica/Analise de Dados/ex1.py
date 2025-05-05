import numpy as np

dados = [58,64,58,56,68,55,68,62,68,50,54,70]
media = np.mean(dados)
mediana = np.median(dados)
conta = dados.count(68)
frequencia = conta/ len(dados)
print(media, mediana, frequencia)