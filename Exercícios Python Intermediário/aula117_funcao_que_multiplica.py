# aula 117
# Closure é quando eu consigo organizar uma função complexa e resumir dentro de uma
# única função (palavra) colocando, por exemplo, função dentro de função
"""
Crie uma função que permita multiplicar um valor em qualquer número
"""

def primeira(x):
    def segunda(y):
        return y*x
    return segunda

duplicar = primeira(2)
triplicar = primeira(3)
quadruplicar = primeira(4)

print(duplicar(3))
print(triplicar(3))
print(quadruplicar(3))
