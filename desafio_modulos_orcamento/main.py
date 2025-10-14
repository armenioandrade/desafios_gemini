# Conforme combinado, o próximo e último tópico de estruturação de código é sobre Módulos e Pacotes. Este é o conceito que permite levar seus sistemas robustos (como o projeto de Orçamento) para o mundo real, separando-o em arquivos e pastas lógicas.

# Vamos retomar o Desafio 30 (Organização do Sistema de Orçamento em módulos).

# 📝 Lembrete do Desafio:
# Você precisa escrever o código de três arquivos separados para o seu sistema de Orçamento:

# dados_basicos.py: Contém as classes Pessoa, Funcionario e Cliente.

# vendas.py: Contém as classes Item e Orcamento.

# main.py: Importa o necessário e executa o código.

import Orcamento

if __name__ == "__main__":
    orc1 = Orcamento('amaro','12345','armenio','armenio.andrade', 1234, 'iphone', 1000)
    orc1.item.adicionar_quantidade(10)
    orc1.gerar_orcamento()