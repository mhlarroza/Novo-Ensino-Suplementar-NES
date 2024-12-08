from typing import List
from .transacao import Transacao               # Importando a classe Transacao para usá-la em nossa conta

                                               # Classe para representar uma conta bancária
class Conta:
    def __init__(self, nome: str) -> None:
        """
        Inicializa uma conta bancária com nome e saldo inicial zero.
        
        :param nome: Nome da conta bancária (ex.: "Conta Corrente")
        """
        self.nome = nome                       # Nome da conta bancária
        self.saldo = 0.0                       # Saldo inicial da conta (começa com 0)
        self.transacoes: List[Transacao] = []  # Lista de transações associadas à conta (inicia vazia)

    def adicionar_transacao(self, valor: float, categoria: str, descricao: str = "") -> Transacao:
        """
        Adiciona uma transação à conta e atualiza o saldo.

        :param valor: Valor da transação (pode ser positivo ou negativo)
        :param categoria: Categoria da transação (ex.: "Salário", "Alimentação")
        :param descricao: Descrição da transação (opcional)
        :return: A transação criada
        """
        transacao = Transacao(valor, categoria, descricao)  # Cria uma nova transação
        self.transacoes.append(transacao)                   # Adiciona a transação à lista de transações
        self.saldo += valor                                 # Atualiza o saldo da conta com o valor da transação
        return transacao                                    # Retorna a transação criada

    def obter_transacoes(self, data_inicial: datetime = None, data_final: datetime = None, categoria: str = None) -> List[Transacao]:
        """
        Filtra e retorna as transações de acordo com critérios de data e categoria.

        :param data_inicial: Data de início para filtrar as transações (opcional)
        :param data_final: Data de fim para filtrar as transações (opcional)
        :param categoria: Categoria para filtrar as transações (opcional)
        :return: Lista de transações que atendem aos critérios
        """
        transacoes_filtradas = self.transacoes                                                   # Começa com todas as transações
        if data_inicial:
            transacoes_filtradas = [t for t in transacoes_filtradas if t.data >= data_inicial]   # Filtra pela data inicial
        if data_final:
            transacoes_filtradas = [t for t in transacoes_filtradas if t.data <= data_final]     # Filtra pela data final
        if categoria:
            transacoes_filtradas = [t for t in transacoes_filtradas if t.categoria == categoria] # Filtra pela categoria
        return transacoes_filtradas                                                              # Retorna a lista filtrada de transações
