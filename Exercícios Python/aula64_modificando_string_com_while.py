# aula 64

"""
Colocando "*" entre as letras do nome digitado
"""

nome = input('Digite seu nome: ')
indice = 0
nova_string = '*'
while indice < len(nome):
  nova_string += nome[indice]
  nova_string += '*'
  indice += 1
print(f'O nome modificado é {nova_string}')
