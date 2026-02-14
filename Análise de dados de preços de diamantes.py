import pandas as pd
import seaborn as sns

#1. Carregar o dataset integrado do Seaborn
df = sns.load_dataset('diamonds')

#2. Visão geral dos dados
print('--- Primeiras 5 linhas ---')
print(df.head())

#3. Estatísticas descritivas dos preços
print('\n--- Resumo Estatístico dos preços (USD) ---')
print(df['price'].describe())

#4. Agrupamento por qualidade do corte (Cut)
print('\n--- Preço médio por qualidade de corte ---')
print(df.groupby('cut')['price'].mean().sort_values(ascending=False))

#5.Correlação simples entre peso (Carat) e preço
correlacao = df['carat'].corr(df['price'])
print(f'\nCorrelação entre Quilates e Preço: {correlacao:.2f}')