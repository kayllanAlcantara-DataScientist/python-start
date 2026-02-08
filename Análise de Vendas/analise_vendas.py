import csv

def carregar_dados(arquivo):
    vendas = []
    with open(arquivo, mode='r', encoding='utf-8') as file:
        leitor = csv.DictReader(file)
        for linha in leitor:
            linha['quantidade'] = int(linha['quantidade'])
            linha['preco'] = float(linha['preco'])
            vendas.append(linha)
    return vendas


def faturamento_total(vendas):
    total = 0
    for venda in vendas:
        total += venda['quantidade'] * venda['preco']
    return total


def produto_mais_vendido(vendas):
    produtos = {}
    for venda in vendas:
        produto = venda['produto']
        produtos[produto] = produtos.get(produto, 0) + venda['quantidade']
    return max(produtos, key=produtos.get)


def receita_por_produto(vendas):
    receitas = {}
    for venda in vendas:
        produto = venda['produto']
        receita = venda['quantidade'] * venda['preco']
        receitas[produto] = receitas.get(produto, 0) + receita
    return receitas


def ticket_medio(vendas):
    total_vendas = sum(v['quantidade'] for v in vendas)
    total_receita = faturamento_total(vendas)
    return total_receita / total_vendas


def gerar_relatorio(vendas):
    print("📊 RELATÓRIO DE VENDAS\n")
    print(f"💰 Faturamento total: R$ {faturamento_total(vendas):.2f}")
    print(f"🏆 Produto mais vendido: {produto_mais_vendido(vendas)}")
    print(f"🧾 Ticket médio: R$ {ticket_medio(vendas):.2f}\n")

    print("📦 Receita por produto:")
    receitas = receita_por_produto(vendas)
    for produto, valor in receitas.items():
        print(f"- {produto}: R$ {valor:.2f}")


def main():
    vendas = carregar_dados("vendas.csv")
    gerar_relatorio(vendas)


if __name__ == "__main__":
    main()
