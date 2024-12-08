import pytest
from financas.conta import Conta
from financas.transacao import Transacao

def test_conta_criacao():
    conta = Conta("Conta Corrente")
    assert conta.nome == "Conta Corrente"
    assert conta.saldo == 0.0
    assert len(conta.transacoes) == 0

def test_adicionar_transacao():
    conta = Conta("Poupança")
    conta.adicionar_transacao(200.0, "Salário", "Salário de novembro")
    assert conta.saldo == 200.0
    assert len(conta.transacoes) == 1
