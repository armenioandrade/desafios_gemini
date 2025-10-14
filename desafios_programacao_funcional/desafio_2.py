# Seu desafio é refatorar os resultados do Desafio 28 usando apenas List Comprehensions.

# Use a mesma lista de vendas: vendas = [150.50, 45.00, 210.75, 99.99, 500.00, 15.00]

# Refatorar map: Calcule a comissão de 10% em uma única List Comprehension.

# Refatorar filter: Selecione apenas as vendas maiores que R$ 100,00 em uma única List Comprehension.

vendas = [150.50, 45.00, 210.75, 99.99, 500.00, 15.00]

comissao = [round(venda * 0.10, 2) for venda in vendas] #o argumento 2 dentro de round() arredonda para duas casas decimais
print(comissao)

vendas_altas = [item_venda for item_venda in vendas if item_venda > 100]
print(vendas_altas)