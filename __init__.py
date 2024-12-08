# Importando as principais classes e funções do pacote para facilitar o uso
from .transacao import Transacao
from .conta import Conta
from .investimento import Investimento
from .cliente import Cliente
from .utilitarios import gerar_relatorio, relatorio_valor_futuro

# Tornando essas classes e funções diretamente acessíveis ao importar o pacote
__all__ = [
    "Transacao",              # Classe Transacao para representar transações financeiras
    "Conta",                  # Classe Conta para representar uma conta bancária
    "Investimento",           # Classe Investimento para representar investimentos financeiros
    "Cliente",                # Classe Cliente para representar um cliente e seus dados financeiros
    "gerar_relatorio",        # Função para gerar relatórios financeiros de um cliente
    "relatorio_valor_futuro"  # Função para gerar relatórios de projeção de valor futuro
]
