# Podemos criar estados dos atributos das instâncias das 
# classes para conseguirmos um melhor controle do 
# fluxo do código. Ex: ligando e acendendo_farol

class Carro(): # self retrata todas as instâncias dessa classe
    
    def __init__(self, nome, ligando=False, acendendo_farol=False):
        self.nome = nome
        self.ligando = ligando
        self.acendendo_farol = acendendo_farol

    def ligar(self):

        if self.ligando:
            print(f'A {self.nome} já está ligada')
            return

        print(f'A {self.nome} está ligando')
        self.ligando = True

    def desligar(self):
        if not self.ligando:
            print(f'A {self.nome} já está desligada')
            return

        print(f'A {self.nome} está desligando')
        self.ligando = False

compass = Carro('Compass')
toro = Carro('Toro')

compass.ligar()
compass.ligar()
compass.ligar()
compass.desligar()
compass.ligar()
compass.desligar()
compass.desligar()
print()
toro.ligar()
toro.desligar()
toro.desligar()