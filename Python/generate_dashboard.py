import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob

def get_latest_file(pattern):
    """Retorna o arquivo mais recente que bate com o padrão"""
    files = glob.glob(pattern)
    if not files:
        raise FileNotFoundError(f"Nenhum arquivo encontrado para o padrão: {pattern}")
    return max(files, key=os.path.getmtime)

def generate_dashboard(problema_path, invoice_path, output_dir):
    invoice_problem_df = pd.read_excel(problema_path)
    plan_df = pd.read_excel(invoice_path).fillna(method="ffill")

    plan_df = plan_df.rename(columns={
        "Item": "Itens",
        "quantidade": "Quantity",
        "Importado?": "National?"
    })

    combined = pd.concat([
        invoice_problem_df[['Itens', 'Quantity', 'Problem', 'National?']],
        plan_df[['Itens', 'Quantity', 'National?']]
    ], ignore_index=True)

    combined['National?'] = (
        combined['National?']
        .astype(str)
        .str.strip()
        .str.replace('*', '', regex=False)
        .str.capitalize()
    )
    combined = combined[combined['National?'].str.lower() != 'nan']

    top_products = combined.groupby('Itens')['Quantity'].sum().sort_values(ascending=False).head(10)

    problem_series = (
        invoice_problem_df['Problem']
        .dropna()
        .str.split('|')
        .explode()
        .str.strip()
    )
    problem_series = problem_series[problem_series != '']
    top_problems = problem_series.value_counts().head(10)

    nationality_counts = combined['National?'].value_counts()

    sns.set_theme()

    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_products.values, y=top_products.index, ax=ax1, palette="viridis")
    ax1.set_title("Top 10 Produtos Mais Pedidos")
    ax1.set_xlabel("Quantidade")
    ax1.set_ylabel("Produto")
    plt.tight_layout()
    fig1.savefig(os.path.join(output_dir, "produtos_mais_pedidos.png"))
    plt.close(fig1)

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_problems.values, y=top_problems.index, ax=ax2, palette="magma")
    ax2.set_title("Problemas Mais Frequentes")
    ax2.set_xlabel("Ocorrências")
    ax2.set_ylabel("Problema")
    plt.tight_layout()
    fig2.savefig(os.path.join(output_dir, "problemas_frequentes.png"))
    plt.close(fig2)

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

    print("Gráficos gerados com sucesso!")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    base_dir = os.path.dirname(script_dir)

    input_dir = os.path.join(base_dir, "Input")
    output_dir = os.path.join(base_dir, "Dashboard")

    os.makedirs(output_dir, exist_ok=True)

    purchase_file = os.path.join(input_dir, "purchase_plan.xlsx")

    problema_file = get_latest_file(os.path.join(input_dir, "invoice_problem_*.xlsx"))

    print(f"📄 Usando arquivos:")
    print(f"  - Problemas (mais recente): {os.path.basename(problema_file)}")
    print(f"  - Plano (fixo):            {os.path.basename(purchase_file)}")

    generate_dashboard(problema_file, purchase_file, output_dir)
    print(f"📊 Imagens salvas em: {output_dir}")