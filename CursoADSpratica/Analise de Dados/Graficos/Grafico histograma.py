# no contexto de estatisticas, o histograma é nada mais q o grafico da função de probabilidade
import panda as pd, matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
#carregando o conjunto de dados california housing
data = fetch_california_housing()
#transformando em um DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)

#gerando o histograma
plt.hist(df["MedInc"])