# aula 113

"""
Crie uma função que receba vários argumentos e retorno o valor de todos esses
argumentos multiplicados. Após isso, exiba o resultado
"""
def multiplicacao(*args):
    total = 1
    for i in range(-1,(-len(args))-1,-1): # não precisava range, apenas colocava args
        total *= args[i]
    return total

resultado = multiplicacao(1,2,3,4,5)
print(resultado)

######################################################################################

"""
Crie uma função que receba um argumento e indique se ele é par ou ímpar
"""

def par_ou_impar(x):
    if x % 2 == 0:
        return f'O número {x} é par'
    return f'O número {x} é ímpar'

verificacao = par_ou_impar(3)
print(verificacao)
        
