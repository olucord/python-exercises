# aula 38

"""
Mostrar qual de dois números é o maior
"""

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
num1 = int(num1)
num2 = int(num2)

if (num1 > num2):
    print('O número 1, "{}", é maior que o número 2, "{}".'.format(num1, num2))
elif (num1 == num2):
    print('O número 1, "{}", é igual ao número 2, "{}".'.format(num1, num2))
else:
    print('O número 2, "{}",'
    ' é maior que o número 1, "{}".'.format(num2, num1))

