import pdfplumber
import pandas as pd

# Caminhos
pdf_path = r"C:\Users\allisson.avila\Documents\GitHub\Python-Study\Estagio\PDFtoXlsx\AIHJAN.pdf"
excel_path = r"C:\caminho\para\saida.xlsx"

# Lista para armazenar os DataFrames de cada página
paginas_dfs = []

# Abrir PDF
with pdfplumber.open(pdf_path) as pdf:
    for i, pagina in enumerate(pdf.pages):
        # Extrair a tabela da página
        tabela = pagina.extract_table()
        if tabela:
            df = pd.DataFrame(tabela[1:], columns=tabela[0])
        else:
            # Se não houver tabela, captura o texto inteiro como uma coluna
            texto = pagina.extract_text().split("\n")
            df = pd.DataFrame(texto, columns=["Texto"])
        paginas_dfs.append((f"Pagina_{i+1}", df))

# Criar arquivo Excel, cada página em uma aba
with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
    for nome_aba, df in paginas_dfs:
        df.to_excel(writer, sheet_name=nome_aba, index=False)

print(f"PDF convertido para Excel em: {excel_path}")
