import pandas as pd
import matplotlib.pyplot as plt

# 1. Configurações
file_name = 'ANALÍTICO INSUMOS ABRIL.xlsx' 

def carregar_dados(caminho):
    if caminho.endswith('.xlsx') or caminho.endswith('.xls'):
        return pd.read_excel(caminho)
    try:
        return pd.read_csv(caminho, sep=None, engine='python', encoding='latin1')
    except:
        return pd.read_csv(caminho, sep=None, engine='python', encoding='utf-8')

df = carregar_dados(file_name)

# 2. Padronização e Limpeza
df.columns = [c.strip().upper() for c in df.columns]
df_items = df.dropna(subset=['ITEM']).copy()
df_items['VALOR'] = pd.to_numeric(df_items['VALOR'], errors='coerce')

def limpar_vol(v):
    v = str(v).upper().replace('L', '').replace(',', '.')
    try: return float(v)
    except: return 0
df_items['VOLUME_NUM'] = df_items['VOLUME'].apply(limpar_vol)

# 3. Lógica de Agrupamento
def agrupar_macro(seg):
    seg = str(seg).upper()
    if 'PROTE' in seg: return 'PROTEÍNA'
    return seg

df_items['CATEGORIA_MACRO'] = df_items['SEGMENTO'].apply(agrupar_macro)

# --- GRÁFICOS ---

# Gráfico 1: 100% do Mês (Sem alterações)
resumo_macro = df_items.groupby('CATEGORIA_MACRO')['VALOR'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 7))
resumo_macro.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='Paired')
plt.title('DISTRIBUIÇÃO TOTAL DE GASTOS - ABRIL')
plt.ylabel('')
plt.tight_layout()
plt.show()

# --- NOVO GRÁFICO 2: AGRUPADO POR TIPO DE PROTEÍNA ---

# Filtramos apenas as proteínas
df_prot_base = df_items[df_items['SEGMENTO'].str.contains('PROTEÍNA', case=False, na=False)].copy()

# Criamos o grupo simplificado (Bovino, Frango, Suíno, Pescado, Ovo)
def simplificar_proteina(seg):
    seg = str(seg).upper()
    if 'BOVINA' in seg: return 'BOVINO'
    if 'FRANGO' in seg: return 'FRANGO'
    if 'SUÍNA' in seg: return 'SUÍNO'
    if 'PESCADO' in seg: return 'PESCADO'
   
    return 'OUTROS'

df_prot_base['TIPO_PROTEINA'] = df_prot_base['SEGMENTO'].apply(simplificar_proteina)

# Agrupamos os dados para somar os valores e volumes
resumo_proteinas = df_prot_base.groupby('TIPO_PROTEINA').agg({
    'VALOR': 'sum',
    'VOLUME_NUM': 'sum'
}).reset_index()

# Calculamos o Custo Médio por KG da categoria
resumo_proteinas['CUSTO_KG_MEDIO'] = resumo_proteinas['VALOR'] / resumo_proteinas['VOLUME_NUM']
resumo_proteinas = resumo_proteinas.sort_values(by='VALOR', ascending=False)

# Plotagem
fig, ax1 = plt.subplots(figsize=(10, 6))

# Barras: Valor total gasto por grupo
ax1.bar(resumo_proteinas['TIPO_PROTEINA'], resumo_proteinas['VALOR'], color='steelblue', alpha=0.7)
ax1.set_ylabel('Gasto Total Acumulado (R$)', fontsize=12)
ax1.set_xlabel('Tipo de Proteína', fontsize=12)

# Linha: Custo Médio por Kg do grupo
ax2 = ax1.twinx()
ax2.plot(resumo_proteinas['TIPO_PROTEINA'], resumo_proteinas['CUSTO_KG_MEDIO'], color='red', marker='o', linewidth=2)
ax2.set_ylabel('Custo Médio R$ / Kg', color='red', fontsize=12)

plt.title('ANÁLISE CONSOLIDADA: GASTO POR TIPO DE PROTEÍNA', fontsize=14)
plt.tight_layout()
plt.show()