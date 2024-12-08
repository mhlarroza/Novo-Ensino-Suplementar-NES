from datetime import datetime
from .cliente import Cliente

def gerar_relatorio(cliente: Cliente) -> str:
    relatorio = f"Relatório financeiro de {cliente.nome}:\n"
    relatorio += f"Patrimônio líquido: R${cliente.calcular_patrimonio_liquido():0.2f}\n"
    relatorio += "Contas:\n"
    for conta in cliente.contas:
        relatorio += f"- {conta.nome}: R${conta.saldo:0.2f}\n"
    relatorio += "Investimentos:\n"
    for investimento in cliente.investimentos:
        relatorio += f"- {investimento.tipo}: R${investimento.calcular_valor():0.2f}\n"
    return relatorio

def relatorio_valor_futuro(cliente: Cliente, data: datetime) -> str:
    relatorio = f"Projeção de valor para {cliente.nome} até {data.strftime('%d/%m/%Y')}:\n"
    total_projecao = 0.0
    for investimento in cliente.investimentos:
        total_projecao += investimento.calcular_valor()
    relatorio += f"Valor futuro estimado: R${total_projecao:0.2f}\n"
    return relatorio
