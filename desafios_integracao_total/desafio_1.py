# Crie um sistema para auditar transações financeiras.

# 1. Classe Componente: Transacao
# Esta classe define a transação.

# Construtor: Recebe _valor. (Use o setter).

# Propriedade (@property e @setter): valor

# Setter: Deve garantir que o valor seja um número positivo (inteiro ou float, mas não negativo ou zero). Se for ≤0, lance um ValueError("O valor da transação deve ser positivo.").

# Se for válido, atribua a self._valor.

# 2. Classe Principal: Auditor
# Esta classe gerencia e registra as transações.

# Construtor: Inicializa uma lista vazia chamada self.transacoes.

# Método de Instância: adicionar_transacao(valor)

# Use um bloco try...except aqui.

# try: Crie uma nova instância de Transacao(valor) e adicione-a à lista self.transacoes.

# except ValueError: Se a criação falhar (o setter da Transacao lançar o erro), imprima: "Falha na Auditoria: Valor inválido detectado. Transação ignorada."

# Método de Instância: gerar_relatorio(nome_arquivo)

# Use o bloco try para lidar com a escrita do arquivo.

# Use with open(nome_arquivo, 'w') as f: para abrir o arquivo.

# Dentro do with, itere sobre self.transacoes. Para cada transação, escreva uma linha no arquivo no formato: VALOR: [valor da transacao]\n.

# else: Se a escrita for 100% bem-sucedida, imprima: "Relatório de auditoria salvo com sucesso."

# finally: Imprima: "Processo de relatório concluído." (Isso deve aparecer sempre).

# Este desafio integra: __init__, Composição, @property, raise ValueError, try/except, e with open.

class Transacao():

    def __init__(self, valor):
        self.valor = valor
    
    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):

        if not isinstance(novo_valor, (int, float)):
            raise TypeError('O valor da transação precisa ser inteiro ou float')
        
        if novo_valor <= 0:
            raise ValueError('O valor da transação deve ser positivo')
          
        self._valor = novo_valor


class Auditor():

    def __init__(self):
        self.transacoes = list()

    def adicionar_transacao(self, valor):
        try:
            transacao = Transacao(valor)
            self.transacoes.append(transacao)
            print(f'Transação de R${transacao.valor:.2f} adicionada.')
        except ValueError:
            print('Falha na Auditoria: Valor inválido detectado. Transação ignorada.')
        except TypeError:
            print('Falha na Auditoria: Tipo inválido detectado. Transação ignorada.')
        except Exception as e:
            print('Erro desconhecido', e)

    def gerar_relatorio(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'w') as f:
                f.write('RELATÓRIO DE TRANSAÇÕES AUDITADAS\n')
                f.write('-' * 30 + '\n')
                for transacao in self.transacoes:
                    linha = f'VALOR: R${transacao.valor:.2f}\n' 
                    f.write(linha)
        except ValueError as v:
                print(v)
        except TypeError as t:
                print(t)
        else:
            print('Relatorio de auditoria salvo com sucesso', nome_arquivo)
        finally:
            print('Processo de relatório concluído')

auditar = Auditor()
auditar.adicionar_transacao(1)
auditar.adicionar_transacao(2)
auditar.adicionar_transacao(3)
auditar.adicionar_transacao(-1)
auditar.adicionar_transacao('a')
auditar.gerar_relatorio('relatorio.txt')

