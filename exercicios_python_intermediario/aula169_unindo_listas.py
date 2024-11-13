# aula 169
# Minha solução está correta, mas o professor
# mostrou novos modos de resolução (função zip 
# e o módulo *itertools* importando zip_longest)

"""
Una as duas listas com base na menor lista, 
não queremos valores "sozinhos" 
"""

list1 = ['Salvador','Ubatuba','Belo Horizonte']
list2 = ['BA','SP','MG', 'RJ']
# Minha solução inicial
list3 = []

if len(list1) <= len(list2):
    for i in range(len(list1)):
        nova = (list1[i],list2[i])
        list3.append(nova)
    print(list3)
else:
    for i in range(len(list2)):
        nova = (list1[i],list2[i])
        list3.append(nova)
    print(list3)
print()
# Usando a função zip
print(zip(list1, list2)) # este retorna o iterador
print()
# Precisamos converter em lista, para ver agindo
print(list(zip(list1, list2))) # este retorna o iterador
print()
# Também podemos unir as listas com base na maior
# mesmo que algum item fique "sozinho" -> zip_longest

from itertools import zip_longest

print(list(zip_longest(list1, list2))) 
print()
# Por padrão o valor que a lista menor não possui
# recebe "None", mas podemos alterá-lo fillvalue

print(list(zip_longest(list1, list2, fillvalue='Sem cidade'))) 
