# Desafio 31: Acumulação de Estoque com reduce()
# O reduce() não é uma função nativa como map e filter; ele precisa ser importado do módulo functools.

# Seu desafio é usar reduce() para calcular o valor total de um estoque.

from functools import reduce

precos = [10.50, 50.00, 15.00, 25.00]
estoque = reduce(lambda x, y: x+y, precos) 
print(estoque)