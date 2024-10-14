# O "*" passa cada valor de uma lista, tupla ou iteráveis como um argumento por vez
# para os parâmetros. Ex: def funcao(*args) e eu chamar assim: funcao(1,2,3,4,5,6,7)
# é como se eu estivesse fazendo na verdade: funcao(1), funcao(2), funcao(3)...
# Para os dicionários é a mesma coisa, só que com **kwargs, porém os "**" transformam
# as chaves como sendo os nomes dos parâmetros enquanto os seus valores serão os argu-
# mentos desses parâmetros. Os ** só fazemo sentido em função ou criando dicts.
# Exemplos práticas abaixo

def soma(a, b, c):
    return a + b + c

numeros = [1, 2, 3] # tivesse 4 números precisaríamos alterar em soma(a, b, c, d) ou soma(*args)
resultado = soma(*numeros)  # desempacota a lista [1, 2, 3] como argumentos individuais
print(resultado)

# Segundo Caso
numeros2 = [1,2,3,4,5,1,26,7,8,9,7,8,4,4,5,65]

def soma2(*args):
    return sum(args)

resultado2 = soma2(*numeros2)
print(resultado)

# Em dicionários

def mostrar_dados(Nome): # não poderia ser 'x'. O nome precisa ser igual a chave com **
    return print(Nome)

dic = {'Nome':'Lucas'}
mostrar_dados(**dic)
# O **dic faz a chave 'Nome' sendo o nome do parâmetro em def mostrar_dados()
# enquanto o valor 'Lucas' será o argumento atribuído a esse parâmetro.

def mostrar_dados2(Nome, Idade): 
    return print(Nome, Idade)

dic = {'Nome':'Lucas', 'Idade':24}
mostrar_dados2(**dic)

# Segundo caso

def mostrar_dados3(**kwargs): 
    return print(kwargs)

dic = {'Nome':'Lucas', 'Idade':24, 'Gênero': 'Masculino', 'Ser':'Humano'}
mostrar_dados3(**dic)

