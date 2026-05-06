import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\fullstack\gestao-de-risco\data\legal_ops_dataset.csv')

print('=== MÉTRICAS PRINCIPAIS ===')
print(f'Total de processos: {len(df):,}')
print(f'Exposição total: R$ {df["valor_causa"].sum():,.0f}')
print(f'Provisionado: R$ {df["valor_provisao"].sum():,.0f}')
print()

print('=== RISCO CPC 25 ===')
for r, c in df['risco_cpc25'].value_counts().items():
    print(f'{r}: {c} ({c/len(df)*100:.1f}%)')
print()

print('=== LEAD TIME ===')
print(f'Médio: {df["lead_time_days"].mean():.0f} dias')
print(f'Mediano: {df["lead_time_days"].median():.0f} dias')
print(f'Máximo: {df["lead_time_days"].max():.0f} dias')
print()

print('=== UF VOLUME ===')
for u, c in df['uf'].value_counts().items():
    print(f'{u}: {c}')
print()

print('=== TIPO DE AÇÃO ===')
for a, c in df['tipo_acao'].value_counts().items():
    print(f'{a}: {c}')
print()

print('=== CUSTO DE DEFESA ===')
print(f'Médio: R$ {df["custo_defesa"].mean():,.0f}')
print(f'Total: R$ {df["custo_defesa"].sum():,.0f}')
ratio = df['custo_defesa'].sum() / df['valor_causa'].sum() * 100
print(f'Custo/Valor: {ratio:.1f}%')
print()

print('=== EFICIÊNCIA POR UF ===')
df['sc_c'] = 1 - df['custo_defesa'] / df['custo_defesa'].max()
df['sc_t'] = 1 - df['lead_time_days'] / df['lead_time_days'].max()
df['sc_r'] = df['risco_cpc25'].map({'Remoto': 1, 'Possível': 0.5, 'Provável': 0})
df['eff'] = (df['sc_c'] + df['sc_t'] + df['sc_r']) / 3 * 100
for u, e in df.groupby('uf')['eff'].mean().sort_values(ascending=False).items():
    print(f'{u}: {e:.1f}')
print()

print('=== RISCO POR UF (% Provável) ===')
risk = df.groupby('uf')['risco_cpc25'].value_counts(normalize=True).unstack().fillna(0)
if 'Provável' in risk.columns:
    for u in risk.sort_values('Provável', ascending=False).index[:5]:
        print(f'{u}: {risk.loc[u, "Provável"]*100:.1f}% provável')
