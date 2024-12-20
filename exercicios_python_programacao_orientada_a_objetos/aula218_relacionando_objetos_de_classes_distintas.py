
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property # getter
    def motor(self):
        return print(self._motor)

    @motor.setter # setter
    def motor(self, valor):
        self._motor = valor

# Essa parte funciona com a parte "Métodos" - linha 52/70

#     def qual_motor(self, motor):
#         print(f'O veículo {self.nome} tem um motor {motor.nome}\n')
    
#     def qual_fabricante(self, fabricante):
#         print(f'O veículo {self.nome} é do fabricante {fabricante.nome}\n')

#     def dados_do_carro(self, motor, fabricante):
#         print(f'O veículo {self.nome} é do fabricante {fabricante.nome}\
#  e tem um motor {motor.nome}\n')

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

# Objetos

c1 = Carro('Toro')
c2 = Carro('Mobi')
c3 = Carro('Compass')
c4 = Carro('Renegade')
c5 = Carro('Commander')

m1 = Motor('2.0 turbo flex')
m2 = Motor('1.0 flex')
m3 = Motor('1.8 turbo flex')
m4 = Motor('2.0 turbo diesel')

f1 = Fabricante('Fiat')
f2 = Fabricante('Jeep')

# Métodos - relacionando objetos de classes distintas

# c5.qual_motor(m4)
# c3.qual_motor(m1)
# c2.qual_motor(m2)
# c1.qual_motor(m4)
# c4.qual_motor(m3)
# print('******************************\n')
# c4.qual_fabricante(f2)
# c2.qual_fabricante(f1)
# c5.qual_fabricante(f2)
# c3.qual_fabricante(f2)
# c1.qual_fabricante(f1)
# print('******************************\n')
# c1.dados_do_carro(m4,f1)
# c2.dados_do_carro(m2,f1)
# c5.dados_do_carro(m4,f2)
# c3.dados_do_carro(m1,f2)
# c4.dados_do_carro(m3,f2)

# Conectando objetos de classes distintas

c1.motor = m4
c1.motor
print(f'\n{c1.__dict__}')


