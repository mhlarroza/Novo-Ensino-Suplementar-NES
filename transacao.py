from datetime import datetime

class Transacao:
    def __init__(self, valor: float, categoria: str, descricao: str = "") -> None:
        self.valor = valor
        self.data = datetime.now()
        self.categoria = categoria
        self.descricao = descricao

    def __str__(self) -> str:
        return f"Transação: {self.descricao} R${self.valor:0.2f} ({self.categoria})"

    def atualizar(self, **atributos) -> None:
        for chave, valor in atributos.items():
            setattr(self, chave, valor)
