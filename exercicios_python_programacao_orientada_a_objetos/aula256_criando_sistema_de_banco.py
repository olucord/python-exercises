# aula 256

"""
Crie um simples sistema de banco. 
Com cliente, conta e banco.
"""

from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome, idade):
        self._nome = nome  
        self._idade = idade

    @property # getter nome
    def nome(self):
        return self._nome

    @property # getter idade
    def idade(self):
        return self._idade

class Cliente(Pessoa):
    def __init__(self, nome, idade, banco):
        super().__init__(nome, idade)
        self.banco = banco
        self.contas = []  

    def abrir_conta(self, conta):
        self.contas.append(conta)


###############################################################################

class Banco():
    lista_de_bancos = []
    def __init__(self, nome):
        self.nome = nome
        Banco.lista_de_bancos.append(self.nome)


###############################################################################

class Conta(ABC):
    def __init__(self, banco_da_conta, agencia, numero_da_conta, saldo):
        self.banco_da_conta = banco_da_conta
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self._saldo = saldo

    @abstractmethod
    def sacar(self, saque): ...

    @property # getter para saldo
    def saldo(self):
        return f'Seu saldo atual é de R$ {self._saldo}'

    def depositar(self, deposito):
        self._saldo += deposito
        print(f'Depósito efetuado com sucesso!')
        print(f'Seu saldo atual é de R$ {self._saldo}\n')

    def __repr__(self):
        return f'{self.banco_da_conta}'
        
class ContaCorrente(Conta):
    limite_de_emprestimo = 1000
    def sacar(self, saque): # limite de (- R$ 1.000)
        if self._saldo - saque > 0:
            self._saldo -= saque
            print(f'{self.banco_da_conta}, sacando {saque}')
            print(f'Seu saldo atual é de R$ {self._saldo}\n')
        elif self._saldo - saque <= 0 and \
self._saldo - saque >= -ContaCorrente.limite_de_emprestimo:
            self._saldo -= saque
            print('\n#########################################')
            print(f'Seu limite atual de crédito é de R$ 1000:')
            print('#########################################\n')
            print(f'{self.banco_da_conta}, sacando {saque}')
            print(f'Seu saldo atual é de R$ {self._saldo}\n')
        else:
            print(f'Você atingiu seu limite atual de crédito\
! Após o pagamento, um novo limite será liberado.\n')

class ContaPoupanca(Conta):
    def sacar(self, saque):
        if self._saldo > 0:
            self._saldo -= saque
            print(f'{self.banco_da_conta}, sacando {saque}')
            print(f'Seu saldo atual é de R$ {self._saldo}\n')
        else:
            print(f'Você não possui saldo suficiente para \
esse saque na {self.banco_da_conta}\n')

 ##############################################################################
# Instâncias

ana = Cliente("Ana",32,'Bradesco')
carlos = Cliente("Carlos",45,'Caixa')
fernanda = Cliente("Fernanda",38,'Santander')
roberto = Cliente("Roberto",57,'Nubank')
cláudia = Cliente("Cláudia",64,'C6bank')

bradesco = Banco('Bradesco')
caixa = Banco('Caixa')
santander = Banco('Santander')
nubank = Banco('Nubank')
c6bank = Banco('C6bank')

conta_bradesco = ContaCorrente('conta_bradesco', 1234, 567890, 1250)
conta_caixa = ContaCorrente('conta_caixa', 5678, 123456, 8910)
conta_santander = ContaCorrente('conta_santander', 9012, 789012, 345)
conta_nubank = ContaCorrente('conta_nubank', 3456, 234567, 3000)
conta_c6bank = ContaCorrente('conta_c6bank', 7890, 345678, 15875)

ana.abrir_conta(conta_bradesco)
carlos.abrir_conta(conta_caixa)
fernanda.abrir_conta(conta_santander)
roberto.abrir_conta(conta_nubank)
cláudia.abrir_conta(conta_c6bank)

print(f'Ana operações:\n')
ana.contas[0].sacar(150)
print(f'Carlos operações:\n')
carlos.contas[0].depositar(200)
print(f'Fernanda operações:\n')
fernanda.contas[0].sacar(18)
print(f'Roberto operações:\n')
roberto.contas[0].sacar(620)
print(f'Cláudia operações:\n')
cláudia.contas[0].sacar(4200)

