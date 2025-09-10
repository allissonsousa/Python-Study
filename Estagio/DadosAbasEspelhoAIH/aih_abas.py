import pandas as pd
import re

CAMINHO_ARQUIVO_AIHS = r"C:\Users\allisson.avila\Documents\GitHub\Python-Study\Estagio\DadosAbasEspelhoAIH\UnirAbas\abasAIH.xlsx"

abas_aih = pd.read_excel(CAMINHO_ARQUIVO_AIHS, sheet_name=None, header=None)

registros_extraidos = []
CBO_ALVO = "225270"

for nome_aba, planilha in abas_aih.items():
    # --- Busca AIH na primeira linha, percorrendo todas as colunas ---
    aih_corrente = None
    for col_idx in range(planilha.shape[1]):
        celula = planilha.iat[0, col_idx]
        if pd.notna(celula):
            # Converte para string e remove espaços
            celula_str = str(celula).strip()
            match = re.search(r'\d{9,11}', celula_str)
            if match:
                aih_corrente = match.group()
                break

    if aih_corrente is None:
        print(f"Aba '{nome_aba}' não contém AIH válido. Pulando...")
        continue
    else:
        print(f"Aba '{nome_aba}' AIH encontrado:", aih_corrente)

    # --- Localiza início da tabela de procedimentos ---
    inicio_tabela_idx = None
    for idx, linha in planilha.iterrows():
        if any(str(cell).strip().upper() == "LINHA PROCED." for cell in linha if pd.notna(cell)):
            inicio_tabela_idx = idx + 1  # próxima linha depois do cabeçalho
            break

    if inicio_tabela_idx is None:
        print(f"Aba '{nome_aba}' não contém tabela de procedimentos. Pulando...")
        continue

    # --- Percorre linhas da tabela ---
    for idx in range(inicio_tabela_idx, len(planilha)):
        linha = planilha.iloc[idx]
        if len(linha) > 2:
            valor_cbo = str(linha[2]).strip()
            if valor_cbo.startswith(CBO_ALVO):
                cns_associado = linha[1] if len(linha) > 1 else None
                registros_extraidos.append([aih_corrente, valor_cbo, cns_associado])

# --- Cria DataFrame final ---
tabela_resultado = pd.DataFrame(registros_extraidos, columns=["AIH", "CBO", "CNS"])

print(tabela_resultado)
tabela_resultado.to_excel("aih_resultados.xlsx", index=False)
