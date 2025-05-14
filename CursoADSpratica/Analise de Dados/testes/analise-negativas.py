import pandas as pd
import os

# Caminho para a pasta onde estão os arquivos .xlsx
pasta = "Este Computador/Documentos/2018"

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