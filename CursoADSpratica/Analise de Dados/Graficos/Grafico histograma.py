# no contexto de estatisticas, o histograma é nada mais q o grafico da função de probabilidade
import pandas as pd, matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
#carregando o conjunto de dados california housing
data = fetch_california_housing()
#transformando em um DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)

#gerando o histograma da variavel medinc
plt.hist(df["MedInc"], bins= 50)
plt.xlabel("MedInc")
plt.ylabel("frequencia")
plt.show()