"""PROPOSTA DO CODIGO:
Carregar um excel com varias abas, coletar os dados de todas as abas e unifica-los em uma tabela única sem repetir
o cabeçalho"""

import pandas as pd
import os


# Caminho do arquivo Excel
arquivo = r"C:\Users\allisson.avila\Documents\GitHub\Python-Study\Estagio\VariasAbasEmUma\UnirAbas\ARQUIVO.xlsx"

# Lê todas as abas (cada aba vira um DataFrame em um dicionário)
todas_abas = pd.read_excel(arquivo, sheet_name=None)

# Concatena todos os DataFrames em um só
unificado = pd.concat(todas_abas.values(), ignore_index=True)

# Salva em uma nova aba dentro do mesmo arquivo
with pd.ExcelWriter("arquivo_unificado.xlsx", engine="openpyxl") as writer:
    unificado.to_excel(writer, sheet_name="Unificado", index=False)

