import matplotlib.pyplot as plt
import numpy as np

#exemplo de dados
#criação de distribuições normais
dados1 = np.random.normal(100,10,200)   #(media, desvio padrao, range de dados)
dados2 = np.random.normal(80,30,200)
dados3 = np.random.normal(90,20,200)
dados4 = np.random.normal(70,25,200)
dados = [dados1, dados2, dados3, dados4]

#plotar o boxplot
plt.boxplot(dados)

#adicionar titulos e legendas
plt.title("Boxplot de dados exemplo")
plt.ylabel("Valores")

#Exibir grafico
plt.show()
