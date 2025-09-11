import pandas as pd
import re
from collections import Counter

CAMINHO_ARQUIVO_AIHS = r"C:\Users\allisson.avila\Documents\GitHub\Python-Study\Estagio\DadosAbasEspelhoAIH\UnirAbas\abasAIH.xlsx"
abas_aih = pd.read_excel(CAMINHO_ARQUIVO_AIHS, sheet_name=None, header=None, dtype=str)

registros_extraidos = []
CBO_ALVO = "225270"

# Colunas para busca de CBO (F até AA = índices 5 a 26)
COL_INICIO, COL_FIM = 5, 26

# CNS
CNS_MIN_LEN, CNS_MAX_LEN = 14, 15

aih_atual = None  # guarda o último AIH válido encontrado

# --- Funções ---
def detectar_aih(linha):
    for col_idx in range(len(linha)):
        celula = linha[col_idx]
        if pd.notna(celula):
            celula_str = str(celula).strip()
            match = re.search(r'\d{7,}-\d', celula_str)
            if match:
                return match.group()
    return None

def detectar_coluna_cbo(planilha, inicio_idx, col_inicio, col_fim):
    scores = Counter()
    for idx in range(inicio_idx, len(planilha)):
        linha = planilha.iloc[idx]
        for col in range(col_inicio, min(col_fim+1, len(linha))):
            val = str(linha[col]).strip() if pd.notna(linha[col]) else ""
            if re.match(r'^\d{6}(\(\d+\))?$', val):
                scores[col] += 1
    if not scores:
        return None
    # pegar coluna com maior score
    max_score = max(scores.values())
    best_cols = [col for col, score in scores.items() if score == max_score]
    return min(best_cols)

def detectar_cns(linha, cbo_idx):
    # verifica todas as colunas antes do CBO
    for col in range(cbo_idx):
        val = linha[col]
        if pd.notna(val):
            s = re.sub(r'\D', '', str(val))
            if CNS_MIN_LEN <= len(s) <= CNS_MAX_LEN:
                return s
    return None

# --- Processamento das abas ---
for nome_aba, planilha in abas_aih.items():
    # Detectar AIH na primeira linha
    aih_corrente = detectar_aih(planilha.iloc[0])
    if aih_corrente:
        aih_atual = aih_corrente
        print(f"Aba '{nome_aba}' AIH detectado: {aih_corrente}")
    else:
        if not aih_atual:
            print(f"Aba '{nome_aba}' sem AIH e nenhum AIH anterior. Pulando...")
            continue
        print(f"Aba '{nome_aba}' sem AIH. Usando AIH anterior: {aih_atual}")

    # Localizar início da tabela
    inicio_tabela_idx = None
    for idx, linha in planilha.iterrows():
        if any(str(cell).strip().upper() == "LINHA PROCED." for cell in linha if pd.notna(cell)):
            inicio_tabela_idx = idx + 1
            break
    if inicio_tabela_idx is None:
        inicio_tabela_idx = 10  # fallback caso não encontre cabeçalho

    # Detectar coluna do CBO
    cbo_col = detectar_coluna_cbo(planilha, inicio_tabela_idx, COL_INICIO, COL_FIM)
    if cbo_col is None:
        print(f"Aba '{nome_aba}' não foi possível detectar coluna CBO. Pulando aba...")
        continue
    print(f"Coluna detectada de CBO: {cbo_col}")

    # Percorrer linhas da tabela
    for idx in range(inicio_tabela_idx, len(planilha)):
        linha = planilha.iloc[idx]
        # Procura CBO na coluna detectada e vizinhas
        found = False
        for col_check in range(max(COL_INICIO, cbo_col-1), min(COL_FIM+1, cbo_col+2)):
            raw_cbo = str(linha[col_check]).strip() if pd.notna(linha[col_check]) else ""
            if not raw_cbo or raw_cbo.lower() == "nan":
                continue
            # captura todos os grupos de 6 dígitos
            for match in re.findall(r'(\d{6})', raw_cbo):
                if match == CBO_ALVO:
                    cns = detectar_cns(linha, col_check)
                    registros_extraidos.append([aih_atual, match, cns])
                    found = True
                    break
            if found:
                break

# --- Resultado final ---
tabela_resultado = pd.DataFrame(registros_extraidos, columns=["AIH", "CBO", "CNS"])
print(tabela_resultado)
tabela_resultado.to_excel("aih_resultados.xlsx", index=False)
