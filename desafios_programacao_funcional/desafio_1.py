# Seu desafio é usar lambda, map(), e filter() para processar uma lista de vendas.

# Considere a seguinte lista de vendas:
# vendas = [150.50, 45.00, 210.75, 99.99, 500.00, 15.00]

# 1. Usando map() (Cálculo de Comissão)
# Use map() com uma lambda para calcular a comissão de 10% sobre cada venda.

# Armazene o resultado em uma lista chamada comissoes.

# 2. Usando filter() (Filtragem de Vendas)
# Use filter() com uma lambda para selecionar apenas as vendas que foram maiores que R$ 100,00.

# Armazene o resultado em uma lista chamada vendas_altas.

vendas = [150.50, 45.00, 210.75, 99.99, 500.00, 15.00]

comissao = list(map(lambda x: round(x * 0.10), vendas))
print(comissao)

vendas_altas = list(filter(lambda x: x > 100.0, vendas))
print(vendas_altas)