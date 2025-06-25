import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Ler os dados brutos
arquivo = "Dados teste.xlsx"
df_raw = pd.read_excel(arquivo, sheet_name="world_olympedia_olympics_athlet", header=None)

# 2. Corrigir: separar os dados que estavam todos juntos em uma única string
df = df_raw[0].str.split(",", expand=True)

# 3. Nomear as colunas corretamente
df.columns = [
    'athlete_id', 'name', 'sex', 'birth_date', 'birth_year',
    'height', 'weight', 'country', 'country_noc',
    'description', 'special_notes'
]

# 4. Manter apenas as primeiras 11 colunas úteis
df = df[df.columns[:11]]

# 5. Remover linhas vazias
df.dropna(how='all', inplace=True)

# 6. Remover duplicados
df.drop_duplicates(inplace=True)

# 7. Mostrar dados nulos
print(df.isnull().sum())

# 8. Top 10 países com mais atletas
print(df['country'].value_counts().head(10))

# 9. Gráfico de distribuição por sexo
sexo = df['sex'].value_counts()
plt.figure(figsize=(5,4))
sexo.plot(kind='bar', color=['lightblue', 'pink'])
plt.title('Distribuição por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Qtd. de Atletas')
plt.tight_layout()
plt.show()

# 10. Gráfico de distribuição do ano de nascimento
df['birth_year'] = pd.to_numeric(df['birth_year'], errors='coerce')
df['birth_year'].dropna().astype(int).plot(kind='hist', bins=20, figsize=(8,4))
plt.title('Distribuição de Anos de Nascimento')
plt.xlabel('Ano')
plt.ylabel('Número de Atletas')
plt.tight_layout()
plt.show()
