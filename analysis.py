import pandas as pd
# Carregar dados
df = pd.read_csv("data/sales.csv")
# Criar coluna de total
df["total"] = df["quantity"] * df["price"]
# Análises básicas
total_vendas = df["total"].sum()
media_vendas = df["total"].mean()
produto_mais_vendido = df.groupby("product")["quantity"].sum().idxmax()
vendas_por_categoria = df.groupby("category")["total"].sum()
print("📊 RELATÓRIO DE VENDAS\n")
print(f"💰 Total de vendas: R$ {total_vendas:.2f}")
print(f"📈 Média de vendas: R$ {media_vendas:.2f}")
print(f"🏆 Produto mais vendido: {produto_mais_vendido}\n")
print("📦 Vendas por categoria:")
print(vendas_por_categoria)
