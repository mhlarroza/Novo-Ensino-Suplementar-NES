from datetime import datetime

# Classe para representar uma transação financeira
class Transacao:
    def __init__(self, valor: float, categoria: str, descricao: str = "") -> None:
        """
        Inicializa a transação com valor, categoria e descrição.
        
        :param valor: Valor da transação (por exemplo, 100.50)
        :param categoria: Categoria da transação (por exemplo, "Alimentação")
        :param descricao: Descrição opcional da transação (por exemplo, "Compra no mercado")
        """
        self.valor = valor  # Valor da transação
        self.data = datetime.now()  # Data e hora da transação (é definida no momento da criação)
        self.categoria = categoria  # Categoria da transação (como "Alimentação", "Transporte", etc)
        self.descricao = descricao  # Descrição da transação (opcional)

    def __str__(self) -> str:
        """
        Retorna uma string formatada com as informações da transação.
        
        :return: String formatada com a descrição, valor e categoria da transação.
        """
        return f"Transação: {self.descricao} R${self.valor:0.2f} ({self.categoria})"

    def atualizar(self, **atributos) -> None:
        """
        Atualiza os atributos da transação com os novos valores fornecidos.

        :param atributos: Argumentos nomeados com os novos valores dos atributos da transação.
        """
        for chave, valor in atributos.items():  # Percorre os atributos fornecidos
            setattr(self, chave, valor)  # Atualiza o valor do atributo da transação com o novo valor
