from abc import ABC, abstractmethod # devem ser importadase

class AbstractFoo(ABC): # AbstractPessoa
    def __init__(self, nome):
        self._nome = None
        self.nome = nome # não "cria" o atributo nome,
# mas apenas ativa o setter do getter "nome"

    @property # getter tem prioridade sobre atributos em chamada
    @abstractmethod
    def nome(self): ... # aqui colocamos apenas a assinatura
# do método, atributos, etc...    

    @nome.setter # setter
    def nome(self, nome):
        self._nome = nome

class Foo(AbstractFoo): # Foo é como se fosse "Pessoa", 
# nesse caso. Foo pode significar qualquer coisa que quisermos     
    
    @property
    def nome(self):
        return self._nome

    @nome.setter # setter
    def nome(self, nome):
        self._nome = nome

p1 = Foo('Lucas')
# p2 = AbstractFoo('Lucas') # não posso instanciar essa classe
print(p1.__dict__)
print(p1.nome)

# OBS: no método "AbstractFoo" "self.nome = nome" está chamando
# o getter "nome" e ativando seu setter "nome"