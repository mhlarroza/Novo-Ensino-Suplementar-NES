from datetime import datetime
from .cliente import Cliente  # Importando a classe Cliente para gerar relatórios financeiros

def gerar_relatorio(cliente: Cliente) -> str:
    """
    Gera um relatório financeiro para um cliente, incluindo saldo das contas e valor dos investimentos.

    :param cliente: O cliente para o qual o relatório será gerado
    :return: Um relatório financeiro formatado como string
    """
    relatorio = f"Relatório financeiro de {cliente.nome}:\n"
    relatorio += f"Patrimônio líquido: R${cliente.calcular_patrimonio_liquido():0.2f}\n"
    relatorio += "Contas:\n"
    for conta in cliente.contas:
        relatorio += f"- {conta.nome}: R${conta.saldo:0.2f}\n"                           # Exibe o nome e saldo das contas
    relatorio += "Investimentos:\n"
    for investimento in cliente.investimentos:
        relatorio += f"- {investimento.tipo}: R${investimento.calcular_valor():0.2f}\n"  # Exibe o tipo e valor atual dos investimentos
    return relatorio                                                                     # Retorna o relatório gerado

def relatorio_valor_futuro(cliente: Cliente, data: datetime) -> str:
    """
    Gera um relatório de projeção de valor futuro para os investimentos de um cliente até uma data fornecida.

    :param cliente: O cliente para o qual o relatório de projeção será gerado
    :param data: A data até a qual o valor futuro será projetado
    :return: Um relatório de valor futuro estimado
    """
    relatorio = f"Projeção de valor para {cliente.nome} até {data.strftime('%d/%m/%Y')}:\n"
    total_projecao = 0.0                                              # Inicializa o valor futuro total com 0
    for investimento in cliente.investimentos:
        total_projecao += investimento.calcular_valor()               # Soma os valores projetados dos investimentos
    relatorio += f"Valor futuro estimado: R${total_projecao:0.2f}\n"  # Exibe o valor futuro estimado
    return relatorio                                                  # Retorna o relatório gerado
