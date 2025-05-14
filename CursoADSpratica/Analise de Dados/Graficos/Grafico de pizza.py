import matplotlib.pyplot as plt, pandas as pd

#grafico de SETORES com distribuição percentual

#criando a tabela

dados = [[1186,1751],[21328,25280],[947,18432],[29,280]]
linhas = ["Estadual","Privada","Municipal","Federal"]
colunas = ["Numero de alunos", "Numero de professores"]
df = pd.DataFrame(dados, columns = colunas, index = linhas)
df["tipo de escola"] = linhas  #adiciona um tipo a escola, nova coluna
print(df)

#criando o grafico
cores = ["tab:red", "tab:green", "tab:blue", "tab:purple"]
dados_alunos = df["Numero de alunos"]
plt.pie(dados_alunos, labels=linhas, colors=cores, autopct="%1.1f%%")
plt.title("Ditribuição do numero de alunos por tipo de escola")
plt.show()