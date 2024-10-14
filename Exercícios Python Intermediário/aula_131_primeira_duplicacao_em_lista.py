# aula 131

"""
Crie uma função que identifique a primeira duplicação de um número em uma lista
Se encontrar repetição, retorne ela. Se não, retorne -1
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

conjunto_sem_repeticao = set()
for lista in lista_de_listas_de_inteiros:
    conjunto_sem_repeticao.clear()
    for num in lista:
        if num in conjunto_sem_repeticao:
            print(num)
            break
        conjunto_sem_repeticao.add(num)
    else:
        print(-1)

# def encontrar_primeira_duplicacao(lista_de_inteiros):
#     conjunto_sem_repeticao = set()
#     for num in lista_de_inteiros:
#         if num in conjunto_sem_repeticao:
#             return print(num)
#         conjunto_sem_repeticao.add(num)
#     return print(-1)

# def encontrar_as_primeiras_duplicacoes(lista_com_lista_de_inteiros):
#     for lista in lista_com_lista_de_inteiros:
#         encontrar_primeira_duplicacao(lista)

# # basta chamar a função abaixo para resolver
# encontrar_as_primeiras_duplicacoes(lista_de_listas_de_inteiros)
