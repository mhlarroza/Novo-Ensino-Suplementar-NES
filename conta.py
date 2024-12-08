from typing import List
from .transacao import Transacao

class Conta:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.saldo = 0.0
        self.transacoes: List[Transacao] = []

    def adicionar_transacao(self, valor: float, categoria: str, descricao: str = "") -> Transacao:
        transacao = Transacao(valor, categoria, descricao)
        self.transacoes.append(transacao)
        self.saldo += valor
        return transacao

    def obter_transacoes(self, data_inicial: datetime = None, data_final: datetime = None, categoria: str = None) -> List[Transacao]:
        transacoes_filtradas = self.transacoes
        if data_inicial:
            transacoes_filtradas = [t for t in transacoes_filtradas if t.data >= data_inicial]
        if data_final:
            transacoes_filtradas = [t for t in transacoes_filtradas if t.data <= data_final]
        if categoria:
            transacoes_filtradas = [t for t in transacoes_filtradas if t.categoria == categoria]
        return transacoes_filtradas
