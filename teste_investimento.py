import pytest
from financas.investimento import Investimento
from financas.conta import Conta

def test_investimento_criacao():
    investimento = Investimento("Tesouro Direto", 1000.0, 0.005)
    assert investimento.tipo == "Tesouro Direto"
    assert investimento.valor_inicial == 1000.0
    assert investimento.taxa_de_rendimento == 0.005
