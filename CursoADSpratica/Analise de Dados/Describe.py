import matplotlib, numpy as np, statistics, pandas as pd
from sklearn.datasets import fetch_california_housing
california = fetch_california_housing()

comprimento = [3,5,6,8,7,3]
variancia = statistics.variance(comprimento)
desvio_padrao = statistics.stdev(comprimento)
amplitude = np.ptp(comprimento)
quantil = np.percentile(comprimento, [25,50,75])

print(variancia)
print(desvio_padrao)
print(amplitude)
print(quantil)

df = pd.DataFrame(california.data, columns= california.feature_names)
df.head()
df.describe()
#sempre use o describe

classes = pd.cut(df['HouseAge'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
freq_classe = classes.value_counts()
print(freq_classe)