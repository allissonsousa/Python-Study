import pandas as pd
import os
import matplotlib.pyplot as plt

# Caminho para a pasta onde estão os arquivos .xlsx
# codigo geral para unir planilhas excel
pasta = r"C:\Users\allisson.avila\Documents\GitHub\Python-Study\Estagio\negativa"

# Lista para armazenar os DataFrames
todas_planilhas = []

# Loop pelos arquivos na pasta
for arq in os.listdir(pasta):
    if arq.endswith(".xlsx"):
        cam_completo = os.path.join(pasta, arq)
        df = pd.read_excel(cam_completo)
        df['Fonte_arquivo'] = arq  # (opcional) adicionar de onde veio cada linha
        todas_planilhas.append(df)

# Concatenar todos os DataFrames
df_unido = pd.concat(todas_planilhas, ignore_index=True)

# Salvar em uma nova planilha
df_unido.to_excel("planilha_unificada.xlsx", index=False)
df = pd.read_excel("planilha_unificada.xlsx")
new = pd.read_excel("planilha_unificada.xlsx", header= None, usecols= [12])


contagem = new.value_counts()

contagem.index = contagem.index.map(lambda x: str(x[0])[:3])

contagem.plot(kind = 'bar', color = 'skyblue')

ax = contagem.plot(kind = 'bar', color = 'skyblue')
ax.bar_label(ax.containers[0], fontsize=8, label_type='edge')
plt.xticks(rotation = 90)
plt.xticks(size = 10)
plt.tight_layout()
plt.grid(True)
plt.show()