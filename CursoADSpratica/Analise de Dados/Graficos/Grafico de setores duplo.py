import matplotlib.pyplot as plt, pandas as pd

# criando a tabela

dados=[[1186, 1751], [21328, 25280], [947, 18432], [29, 280]]
linhas = ["Estadual", "Privada", "Municipal", "Federal"]
colunas = ["Numero de alunos", "Numero de professores"]
df = pd.DataFrame(dados, columns=colunas, index=linhas)
"""df["tipo de escola"] = linhas  # adiciona um tipo a escola, nova coluna"""
print(df)

#uso da funçao subplots

fig, axs = plt.subplots(1,2, figsize=(8,4))
df.plot.pie(y = "Numero de alunos", ax=axs[0], autopct="%1.1f%%", colors = ["blue", "green", "orange", "red"],labels=None)
axs[0].set_title("Número de alunos por tipo de escola")

df.plot.pie(y="Numero de professores", ax=axs[1], autopct="%1.1f%%", colors = ["blue", "green", "orange", "red"],labels=None)
axs[1].set_title("Número de Professores por tipo de escola")

plt.tight_layout()
plt.show()

"""
autopct -- define o formato da porcentagem
plt.tihht -- ajusta automaticamente o epaço entre os graficos
labels=none --- deixa as fatia de pixa sem nome, ja q o grafico ja tem legenda"""