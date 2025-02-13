# aula 171
# Professor resolveu mais fácil, eu improvisei
# Se quisermos somar todos os valores das duas 
# listas, podemos usar zip_longest e somar com 
# zero (fillvalue=0) para os items "sozinhos"

"""
Some as duas listas, com iterações baseadas na menor
"""

list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7]

# Minha solução
list3 = [
    list1[i]+list2[i]
    for i in range( # mais fácil usar *Min* para checar
        len(list1) if len(list1) <= len(list2) 
        else len(list2))
]
print(list3)

print()

# Professor
list4 = [x + y for x, y in list(zip(list1, list2))]
print(list4)