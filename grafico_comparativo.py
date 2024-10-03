import pandas as pd
import matplotlib.pyplot as plt

# Carregando as planilhas de vendas
vendas_2023_janeiro = pd.read_excel('vendas_2023.xlsx', sheet_name='janeiro')
vendas_2023_fevereiro = pd.read_excel('vendas_2023.xlsx', sheet_name='fevereiro')
vendas_2024_janeiro = pd.read_excel('vendas_2024.xlsx', sheet_name='janeiro')
vendas_2024_fevereiro = pd.read_excel('vendas_2024.xlsx', sheet_name='fevereiro')

# Suponha que temos uma coluna chamada 'total_vendas' em cada DataFrame
# Vamos pegar os totais de vendas para o gráfico
totais_2023 = [
    vendas_2023_janeiro['total_vendas'].sum(),
    vendas_2023_fevereiro['total_vendas'].sum()
]

totais_2024 = [
    vendas_2024_janeiro['total_vendas'].sum(),
    vendas_2024_fevereiro['total_vendas'].sum()
]

# Configurando os dados para o gráfico
meses = ['Janeiro', 'Fevereiro']
largura = 0.35  # Largura das barras

# Criando o gráfico de barras
fig, ax = plt.subplots()
barras1 = ax.bar(meses, totais_2023, largura, label='2023')
barras2 = ax.bar([meso for meso in meses], totais_2024, largura, label='2024', bottom=totais_2023)

# Adicionando detalhes ao gráfico
ax.set_ylabel('Total de Vendas')
ax.set_title('Comparativo de Vendas de Janeiro e Fevereiro')
ax.legend()

# Exibindo o gráfico
plt.show()
