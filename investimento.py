from datetime import datetime
from typing import Optional
from .conta import Conta

class Investimento:
    def __init__(self, tipo: str, valor_inicial: float, taxa_de_rendimento: float, data_compra: Optional[datetime] = None) -> None:
        self.tipo = tipo
        self.valor_inicial = valor_inicial
        self.data_compra = data_compra or datetime.now()
        self.taxa_de_rendimento = taxa_de_rendimento
        self.cliente = None  # Será associado posteriormente ao cliente

    def calcular_valor(self) -> float:
        # Lógica para calcular o valor do investimento com base no tempo
        meses_decorridos = (datetime.now() - self.data_compra).days // 30
        return self.valor_inicial * (1 + self.taxa_de_rendimento) ** meses_decorridos

    def vender(self, conta: Conta) -> None:
        valor = self.calcular_valor()
        conta.saldo += valor
        conta.adicionar_transacao(valor, "Venda de Investimento", f"Venda do investimento {self.tipo}")
