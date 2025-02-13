print("\nAssociação*************************************************************\n")

# ASSOCIAÇÃO - apenas mostra que dois objetos entre duas classes
# estão conectados entre si (um "conhece" o outro)

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None

class Motorista:
    def __init__(self, nome):
        self.nome = nome

    def dirigindo(self):
        return f'{self.nome} está dirigindo'

compass = Carro('Compass')		
marinho = Motorista('Marinho')		
		
compass.ferramenta = marinho		
print(compass.ferramenta.dirigindo())		

print("\nAgregação*************************************************************\n")

# AGREGAÇÃO - mostra que dois objetos independentes de classes
# diferentes podem interagir entre si, executando uma ação 
# maior entre eles. Ex: um "carro" + "pneu" (ou pneus). Exemplo 
# do professor, "carrinho de compras" + "produtos" (os dois 
# juntos fazem mais sentido do que sozinhos) 

class Carrinho: # Imagine um carrinho de compras
    def __init__(self):
        self.lista = [] # armazena referências as instâncias p1, p2
# se printar, mostra onde essas referências estão armazenadas na 
# memória
    def inserir(self, produto):
        self.lista.append(produto)

    def listar(self):
        for p in self.lista: # como adicionamos uma referência a uma 
# instância de outra classe na lista dessa classe, também temos acesso
# as referências dos atributos dessa instância (não temos acesso ao 
# atributo em si, apenas podemos "referencia-lo/vizualiza-lo")
            print(p.nome, p.preco)

    def total(self):
        total = 0
        for p in self.lista:
            total += p.preco
        return print(f'O total é R$ {total}')
        

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1 = Produto('Leite', 8.65)
p2 = Produto('Iogurte', 10.5)
carrinho.inserir(p1)
carrinho.inserir(p2)

print(f'{carrinho.lista}\n\n')
carrinho.total()

print("\nComposição*************************************************************\n")

# COMPOSIÇÃO - é uma especialização da agregação e, consequentemente, 
# da associação. Os objetos aqui apresentam uma relação mais forte 
# que as outras, pois quando o objeto "pai" (principal) for deletado, 
# os outros objetos a ele associados serão apagados junto.
# É preciso criar uma instância dentro de outra classe. Assim
# ela será apagada junto quando a instância de referência for deletada.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
        
    def adicionar_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def adicionar_enderecos_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
    
    def __del__(self):
        print(f'A instância de pessoa foi apagada')


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print(f'A instância de endereço foi apagada')

p1 = Pessoa('Letícia', 32)
p1.adicionar_enderecos('Rua Castro Alves', 418)
p1.adicionar_enderecos('Rua Belinda Clarke', 9072)
p1.adicionar_enderecos('Av Pedro Nascimento', 261)
e4 = Endereco('Rua Bafo de Bode', 24)
p1.adicionar_enderecos_externo(e4)
p1.listar_enderecos()
print(f'\n{p1.enderecos}\n') # são as referências as instâncias criadas
print('A instância de pessoa leva junto os endereços da mesma classe\
 - COMPOSIÇÃO:\n')
del p1 # os endereços são apagados junto da pessoa, pois pertecem a mesma
# classe
print('\nFim do código. Todas seriam apagadas de todo jeito após o código\
 finalizar\n')

# Observe que as instâncias não receberam "apelidos", pois foram criadas
# dentro do método na classe Pessoa. Mas é como se fossem "e1", "e2" e "e3"...,
# isto é, se recebessem alguma variável como atribuição