import matplotlib.pyplot as plt, pandas as pd

#criando a tabela

dados = [[1186,1751],[21328,25280],[947,18432],[29,280]]
linhas = ["Estadual","Privada","Municipal","Federal"]
colunas = ["Numero de alunos", "Numero de professores"]
df = pd.DataFrame(dados, columns = colunas, index = linhas)
df["tipo de escola"] = linhas  #adiciona um tipo a escola, nova coluna
print(df)

#criando o grafico

x = df["Numero de Professores"]
y = df["Numero de alunos"]
plt.scatter(x,y)
plt.title("Relação entre Numero de Professores e Numero de alunos")
plt.xlabel("Numero de Professores")
plt.ylabel("Numero de alunos")
plt.show()
