import matplotlib.pyplot as plt, pandas as pd

#criando a tabela

dados = [[1186,1751],[21328,25280],[947,18432],[29,280]]
linhas = ["Estadual","Privada","Municipal","Federal"]
colunas = ["Numero de alunos", "Numero de professores"]
df = pd.DataFrame(dados, columns = colunas, index = linhas)
df["tipo de escola"] = linhas  #adiciona um tipo a escola, nova coluna
print(df)

#criando o grafico
df.plot.barh(x = "tipo de escola",y = "Numero de alunos",orientation="horizontal", color= "green")
plt.title("Numero de alunos por tipo de escola")
plt.xlabel("tipo de escola")
plt.ylabel("Numero de alunos")
plt.show()