import pytest
from financas.cliente import Cliente
from financas.conta import Conta

def test_cliente_criacao():
    cliente = Cliente("João")
    assert cliente.nome == "João"
    assert len(cliente.contas) == 0
    assert len(cliente.investimentos) == 0

def test_adicionar_conta():
    cliente = Cliente("Maria")
    conta = cliente.adicionar_conta("Conta Poupança")
    assert len(cliente.contas) == 1
    assert conta.nome == "Conta Poupança"
