# aula 160
# Professor resolveu usando Closure, eu improvisei 
# com input e interação, mas ele queria que o pro-
# gramador que passasse o segundo argumento "y"

"""
A função quando é chamada diretamente, ela vai 
executar o código, mas queremos que ela não 
execute na hora e sim armazene a variável na memória
"""

def somar(x):
    try:
        y = int(input('Digite o número que você'\
                      ' quer somar cinco: '))
        return x + y
    except:
        print('Você digitou uma expressão inválida.')

def multiplicar(x,y):
    return x * y

def executar(funcao, *args):
    return funcao(*args)

somar_com_cinco = executar(somar, 5)
print(somar_com_cinco)
