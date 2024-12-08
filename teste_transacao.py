import pytest
from financas.transacao import Transacao
from datetime import datetime

def test_transacao_criacao():
    t = Transacao(100.50, "Alimentação", "Compra no mercado")
    assert t.valor == 100.50
    assert t.categoria == "Alimentação"
    assert t.descricao == "Compra no mercado"
    assert isinstance(t.data, datetime)

def test_transacao_str():
    t = Transacao(50.75, "Transporte", "Passagem de ônibus")
    assert str(t) == "Transação: Passagem de ônibus R$50.75 (Transporte)"

def test_transacao_atualizar():
    t = Transacao(100, "Lazer", "Cinema")
    t.atualizar(valor=150, descricao="Cinema IMAX")
    assert t.valor == 150
    assert t.descricao == "Cinema IMAX"
