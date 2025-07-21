import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import argparse

def generate_dashboard(problema_path, invoice_path, output_dir):
    # Carregar os dados
    invoice_problem_df = pd.read_excel(problema_path)  # Planilha apenas com problemas
    plan_df = pd.read_excel(invoice_path).fillna(method="ffill")  # Tratamento das células mescladas

    # Renomear colunas do plano
    plan_df = plan_df.rename(columns={
        "Item": "Itens",
        "quantidade": "Quantity",
        "Importado?": "National?"
    })

    # Unificar dados
    combined = pd.concat([
        invoice_problem_df[['Itens', 'Quantity', 'Problem', 'National?']],
        plan_df[['Itens', 'Quantity', 'National?']]
    ], ignore_index=True)

    # Limpeza: normalizar 'National?' e remover valores inválidos
    combined['National?'] = (
        combined['National?']
        .astype(str)
        .str.strip()
        .str.replace('*', '', regex=False)
        .str.capitalize()
    )
    # Remove "nan" literal
    combined = combined[combined['National?'].str.lower() != 'nan']

    # Produtos mais pedidos
    top_products = combined.groupby('Itens')['Quantity'].sum().sort_values(ascending=False).head(10)

    # Problemas mais comuns (direto da planilha de problemas)
    problem_series = (
        invoice_problem_df['Problem']
        .dropna()               # Remove NaN
        .str.split('|')         # Divide múltiplos problemas
        .explode()              # Transforma em linhas separadas
        .str.strip()            # Remove espaços extras
    )
    # Remove entradas vazias
    problem_series = problem_series[problem_series != '']
    top_problems = problem_series.value_counts().head(10)

    # Nacional x Importado
    nationality_counts = combined['National?'].value_counts()

    sns.set_theme()

    # 1. Produtos mais pedidos
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_products.values, y=top_products.index, ax=ax1, palette="viridis")
    ax1.set_title("Top 10 Produtos Mais Pedidos")
    ax1.set_xlabel("Quantidade")
    ax1.set_ylabel("Produto")
    plt.tight_layout()
    fig1.savefig(os.path.join(output_dir, "produtos_mais_pedidos.png"))
    plt.close(fig1)

    # 2. Problemas mais comuns
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_problems.values, y=top_problems.index, ax=ax2, palette="magma")
    ax2.set_title("Problemas Mais Frequentes")
    ax2.set_xlabel("Ocorrências")
    ax2.set_ylabel("Problema")
    plt.tight_layout()
    fig2.savefig(os.path.join(output_dir, "problemas_frequentes.png"))
    plt.close(fig2)

    # 3. Nacional vs Importado
    fig3, ax3 = plt.subplots(figsize=(6, 6))
    ax3.pie(
        nationality_counts,
        labels=nationality_counts.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=['#8BC34A', '#FF9800']
    )
    ax3.axis('equal')
    fig3.suptitle("Produtos Nacionais vs Importados")
    plt.tight_layout()
    fig3.savefig(os.path.join(output_dir, "nacional_vs_importado.png"))
    plt.close(fig3)

    return "✅ Gráficos gerados com sucesso!"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gera gráficos com base em arquivos de invoice e plano de compra.")
    parser.add_argument('--problema_path', required=True)
    parser.add_argument('--invoice_path', required=True)
    parser.add_argument('--output_dir', required=True)

    args = parser.parse_args()
    resultado = generate_dashboard(args.problema_path, args.invoice_path, args.output_dir)
    print(resultado)
