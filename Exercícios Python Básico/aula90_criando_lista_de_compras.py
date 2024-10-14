# aula 90

"""
Criar uma lista de compras onde o usuário pode inserir, apagar e listar
quais são os itens inseridos na lista
"""

import os
lista_de_compras = []
escolha = None

while True:
    escolha = input('Inserir (i), apagar (a) ou listar (l): ')
    if escolha == '' or len(escolha) > 1:
        os.system('cls')
        print('Você precisa escolher uma das opções abaixo.')
        continue
    if escolha == 'i':
        item = input('Digite o item a inserir: ')
        lista_de_compras.append(item)
        continue
    elif escolha == 'a':
        try:
            indice_item_apagar = input('Digite o índice do item a apagar: ')
            del lista_de_compras[int(indice_item_apagar)]
        except:
            print('Não foi possível apagar o item')
            continue
        continue
    elif escolha == 'l':
        os.system('cls')
        if not lista_de_compras:
            print('Não há itens na lista')
            continue
        for indice,nome in enumerate(lista_de_compras):
            print(indice, nome)
            continue   
    else:
        os.system('cls')
        print('Você precisa escolher uma das opções abaixo.')
        continue
