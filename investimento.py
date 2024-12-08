from datetime import datetime
from typing import Optional
from .conta import Conta  # Importando a classe Conta para associar investimentos a uma conta

                          # Classe para representar um investimento financeiro
class Investimento:
    def __init__(self, tipo: str, valor_inicial: float, taxa_de_rendimento: float, data_compra: Optional[datetime] = None) -> None:
        """
        Inicializa um investimento com tipo, valor inicial, taxa de rendimento e data de compra.

        :param tipo: Tipo do investimento (ex.: "Tesouro Direto", "CDB")
        :param valor_inicial: Valor inicial investido
        :param taxa_de_rendimento: Taxa de rendimento mensal do investimento
        :param data_compra: Data da compra do investimento (se não fornecida, usa a data atual)
        """
        self.tipo = tipo                                  # Tipo do investimento (ex.: "Tesouro Direto")
        self.valor_inicial = valor_inicial                # Valor inicial do investimento
        self.data_compra = data_compra or datetime.now()  # Data da compra (se não fornecida, usa a data atual)
        self.taxa_de_rendimento = taxa_de_rendimento      # Taxa de rendimento mensal do investimento
        self.cliente = None                               # O cliente será associado depois ao investimento

    def calcular_valor(self) -> float:
        """
        Calcula o valor atual do investimento com base no tempo passado desde a compra.

        :return: Valor atual do investimento após o cálculo de rendimento
        """
        meses_decorridos = (datetime.now() - self.data_compra).days // 30              # Calcula o número de meses desde a compra
        return self.valor_inicial * (1 + self.taxa_de_rendimento) ** meses_decorridos  # Calcula o valor do investimento com base na taxa de rendimento

    def vender(self, conta: Conta) -> None:
        """
        Vende o investimento e deposita o valor resultante na conta fornecida.

        :param conta: A conta onde o valor será depositado após a venda do investimento
        """
        valor = self.calcular_valor()                                                                    # Calcula o valor do investimento no momento da venda
        conta.saldo += valor                                                                             # Depósito do valor do investimento na conta
        conta.adicionar_transacao(valor, "Venda de Investimento", f"Venda do investimento {self.tipo}")  # Criação de uma transação para registrar a venda
