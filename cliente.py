from typing import List
from .conta import Conta                # Importando a classe Conta para o cliente poder ter contas
from .investimento import Investimento  # Importando a classe Investimento para o cliente poder ter investimentos

                                        # Classe para representar um cliente, com suas contas e investimentos
class Cliente:
    def __init__(self, nome: str) -> None:
        """
        Inicializa o cliente com um nome e listas de contas e investimentos vazias.
        
        :param nome: Nome do cliente (ex.: "João", "Maria")
        """
        self.nome = nome                             # Nome do cliente
        self.contas: List[Conta] = []                # Lista de contas do cliente (inicialmente vazia)
        self.investimentos: List[Investimento] = []  # Lista de investimentos do cliente (inicialmente vazia)

    def adicionar_conta(self, nome_conta: str) -> Conta:
        """
        Adiciona uma conta ao cliente.
        
        :param nome_conta: Nome da conta a ser criada (ex.: "Conta Corrente")
        :return: A conta criada
        """
        conta = Conta(nome_conta)  # Cria uma nova conta com o nome fornecido
        self.contas.append(conta)  # Adiciona a conta à lista de contas do cliente
        return conta               # Retorna a conta criada

    def adicionar_investimento(self, investimento: Investimento) -> None:
        """
        Adiciona um investimento ao cliente.

        :param investimento: O investimento a ser adicionado
        """
        self.investimentos.append(investimento)  # Adiciona o investimento à lista de investimentos do cliente
        investimento.cliente = self              # Associa o cliente ao investimento

    def calcular_patrimonio_liquido(self) -> float:
        """
        Calcula o patrimônio líquido do cliente somando o saldo de todas as contas e o valor atual de todos os investimentos.

        :return: O patrimônio líquido do cliente
        """
        total = sum(conta.saldo for conta in self.contas)                                   # Soma o saldo de todas as contas
        total += sum(investimento.calcular_valor() for investimento in self.investimentos)  # Soma o valor de todos os investimentos
        return total                                                                        # Retorna o patrimônio líquido total
