import matplotlib.pyplot as plt

# Dados
proteinas = ['Frango', 'Carne Bovina', 'Pescados', 'Suínos']
kg = [464, 275.8, 80.9, 53]
custo = [6760.00, 9971.88, 4376.24, 2338.71]

# Percentual
total = sum(custo)
percentuais = [(c / total) * 100 for c in custo]

# Cores
cor_kg = '#4C78A8'
cor_custo = '#F58518'

fig, axs = plt.subplots(1, 2, figsize=(14,5))
fig.suptitle('Proteínas', fontsize=18, weight='bold')

# ===== Gráfico 1: KG =====
axs[0].bar(proteinas, kg, color=cor_kg, width=0.5)  # 👈 aqui

axs[0].set_title('Volume (Kg)', fontsize=12)
axs[0].grid(axis='y', linestyle='--', alpha=0.3)
axs[0].margins(x=0.2)  # 👈 mais espaço lateral

for spine in axs[0].spines.values():
    spine.set_visible(False)

for i, v in enumerate(kg):
    axs[0].text(i, v, f'{v:.1f}',
                ha='center', va='bottom', fontsize=10)

# ===== Gráfico 2: CUSTO =====
axs[1].bar(proteinas, custo, color=cor_custo, width=0.5)  # 👈 aqui

axs[1].set_title('Custo (R$)', fontsize=12, pad=20)
axs[1].grid(axis='y', linestyle='--', alpha=0.3)
axs[1].margins(x=0.2)  # 👈 mais espaço lateral

for spine in axs[1].spines.values():
    spine.set_visible(False)

for i, v in enumerate(custo):
    texto = f'R$ {v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    
    axs[1].text(i, v,
                f'{texto}\n({percentuais[i]:.1f}%)',
                ha='center', va='bottom', fontsize=10)

plt.tight_layout(rect=[0, 0, 1, 0.92])
plt.show()