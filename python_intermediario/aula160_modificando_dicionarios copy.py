# aula 160

"""
Primeiro: aumente em 10% os preços dos produtos da lista
Segundo: Gere novos produtos por deepy copy (cópia profunda)
Terceiro: Ordene os produtos por nome decrescente
Quarto: Gere produtos ordenados por nome com deepy copy (cópia profunda)
Quinto: Ordene os produtos por preço crescente
Sexto: Gere produtos ordenados por preço com deepy copy (cópia profunda)
"""

import copy # se for grande, copia apenas uma parte

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

print('Lista inicial:', end='\n\n')
print(*produtos, sep='\n', end='\n\n')

# Primeira: aumente em 10% os preços dos produtos da lista

for dic in produtos:
    dic['preco'] = round(dic['preco']*1.1, 2)
print('Aumento de 10% nos preços:', end='\n\n')
print(*produtos, sep='\n', end='\n\n')    

# Segunda: Gere novos produtos por deepy copy (cópia profunda)

novos_produtos = copy.deepcopy(produtos)
print('Deepy Copy com preço alterado:', end='\n\n')
print(*novos_produtos, sep='\n', end='\n\n')    

# Terceira: Ordene os produtos por nome decrescente

# Função que ordena os dicionários da lista
def ordena_lista_de_dicionarios(dic_da_lista):
    return dic_da_lista['nome']

# sort com reverse = True para decrescente
produtos.sort(key=ordena_lista_de_dicionarios, reverse=True)
print('Produtos ordenados por nome decrescente:', end='\n\n')
print(*produtos, sep='\n', end='\n\n')

# Quarta: Gere produtos ordenados por nome com deepy copy (cópia profunda)

novos_produtos_ordenados_por_nome = copy.deepcopy(produtos)

print('Deepy Copy ordenado por nome:', end='\n\n')
print(*novos_produtos_ordenados_por_nome, sep='\n', end='\n\n')

# Quinta: Ordene os produtos por preço crescente

# Função que ordena os dicionários da lista
def ordena_lista_de_dicionarios_2(dic_da_lista):
    return dic_da_lista['preco']

produtos.sort(key=ordena_lista_de_dicionarios_2)

print('Produtos ordenados por preço crescente:', end='\n\n')
print(*produtos, sep='\n', end='\n\n')

# Sexta: Gere produtos ordenados por preço com deepy copy (cópia profunda)

novos_produtos_ordenados_por_preco = copy.deepcopy(produtos)

print('Deepy Copy ordenado por preço:', end='\n\n')
print(*novos_produtos_ordenados_por_preco, sep='\n', end='\n\n')
