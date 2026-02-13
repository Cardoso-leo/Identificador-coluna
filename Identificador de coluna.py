import pandas as pd
import os
import glob

# =====================================
# PASTA ONDE ESTÁ O ARQUIVO NOVO
# =====================================
PASTA = r"\\192.168.200.81\C6Bank-Gestao\Planejamento C6\0. Reports\4. Enriquecimento\2026\01. Janeiro\Honda\2. Enriquecido\LAYOUT 2"

# =====================================
# BUSCA AUTOMÁTICA DE ARQUIVOS
# =====================================
arquivos = []
arquivos.extend(glob.glob(os.path.join(PASTA, "*.csv")))
arquivos.extend(glob.glob(os.path.join(PASTA, "*.xlsx")))
arquivos.extend(glob.glob(os.path.join(PASTA, "*.xls")))

if not arquivos:
    raise FileNotFoundError("Nenhum arquivo CSV ou Excel encontrado na pasta.")

# Pega o mais recente
ARQUIVO = max(arquivos, key=os.path.getmtime)

print(f"\n📂 Arquivo selecionado automaticamente:")
print(ARQUIVO)

# =====================================
# LEITURA INTELIGENTE
# =====================================
ext = os.path.splitext(ARQUIVO)[1].lower()

if ext == ".csv":
    try:
        df = pd.read_csv(ARQUIVO, sep=";", encoding="utf-8", low_memory=False)
    except:
        print("⚠ Tentando separador ',' ...")
        df = pd.read_csv(ARQUIVO, sep=",", encoding="utf-8", low_memory=False)

elif ext in [".xlsx", ".xls"]:
    df = pd.read_excel(ARQUIVO)

else:
    raise ValueError(f"Formato '{ext}' não suportado.")

# =====================================
# NORMALIZAÇÃO
# =====================================
df.columns = df.columns.astype(str).str.strip()

# =====================================
# RESULTADO
# =====================================
print("\n" + "="*60)
print("📌 TOTAL DE COLUNAS:", len(df.columns))
print("="*60)

print("\n📌 NOMES DAS COLUNAS:")
for i, col in enumerate(df.columns, start=1):
    print(f"{i:02d} - {col}")

print("\n📌 TIPOS DE DADOS:")
print(df.dtypes)

print("\n📌 PRIMEIRAS 5 LINHAS:")
print(df.head())

print("\n✅ Fim da análise.")
