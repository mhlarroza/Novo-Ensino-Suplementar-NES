from typing import List
from .conta import Conta
from .investimento import Investimento

class Cliente:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.contas: List[Conta] = []
        self.investimentos: List[Investimento] = []

    def adicionar_conta(self, nome_conta: str) -> Conta:
        conta = Conta(nome_conta)
        self.contas.append(conta)
        return conta

    def adicionar_investimento(self, investimento: Investimento) -> None:
        self.investimentos.append(investimento)
        investimento.cliente = self

    def calcular_patrimonio_liquido(self) -> float:
        total = sum(conta.saldo for conta in self.contas)
        total += sum(investimento.calcular_valor() for investimento in self.investimentos)
        return total
