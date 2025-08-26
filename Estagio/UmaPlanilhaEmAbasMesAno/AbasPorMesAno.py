import pandas as pd
import openpyxl
from pathlib import Path
import re

#Nomes dos meses em Portugues para nomear cada aba do arquivo
MONTH_NAMES_PT = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]
def sanitize_sheet_name(sheet_name):
