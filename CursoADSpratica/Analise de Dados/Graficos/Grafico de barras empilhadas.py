import matplotlib.pyplot as plt, pandas as pd

#criando a tabela

dados = [[1186,1751],[21328,25280],[947,18432],[29,280]]
linhas = ["Estadual","Privada","Municipal","Federal"]
colunas = ["Numero de alunos", "Numero de professores"]
df = pd.DataFrame(dados, columns = colunas, index = linhas)
df["tipo de escola"] = linhas  #adiciona um tipo a escola, nova coluna
print(df)

#criando o grafico

ax = df.plot.barh(stacked = True)
plt.title("Distribuição deNumero de alunos e professores por tipo de escola")
plt.xlabel("tipo de escola")
plt.ylabel("Numero de individuos")
plt.legend(loc= "upper right")
plt.show()
