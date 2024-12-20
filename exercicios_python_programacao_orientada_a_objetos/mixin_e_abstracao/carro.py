from telefone import TelefonarMaeMixin 

class Carro:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano

    def ligar_carro(self):
        print(f'{self.nome} está ligando')

class Compass(Carro, TelefonarMaeMixin):
    ...

class Toro(Carro, TelefonarMaeMixin):
    ...

class Renegade(Carro, TelefonarMaeMixin):
    ...

compass = Compass('Compass', 2018)

print('Métodos e atributos da classe superior Carro (classe "mãe")')
print()
print(f'Nome do veículo: {compass.nome}')
print(f'Ano do veículo: {compass.ano}')
compass.ligar_carro()
print()
print('Métodos e atributos do mixin TelefonarMaeMixin')
print()
compass.telefonar()
print()
print('Agora o carro tem uma nova "funcionalidade". Ele também\
 faz ligações para pessoas "sem ter um celular"')
print() # Este é o papel de um mixin


