

class ErroDeNumero(Exception): # criando o erro "ErroDeNumero"
    def __init__(self, mensagem_de_erro):
        super().__init__(mensagem_de_erro)

class Telefone:
    def _telefonar(self):
        raise ErroDeNumero('Nenhum contato selecionado. \
Implemente o método de telefonar')
    
    def telefonar(self):
        return self._telefonar()

class TelefonarMaeMixin(Telefone):
    def _telefonar(self):
        print('Ligando para mãe')

class TelefonarPaiMixin(Telefone):
    def _telefonar(self):
        print('Ligando para pai')

if __name__ == '__main__':
    chamador = TelefonarMaeMixin()
    chamador.telefonar()