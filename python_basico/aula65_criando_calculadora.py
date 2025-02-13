# aula 65
# OBS: Na aula o professor usa o while criando um loop de cálculos infinitos 
# com o (while True:) até o usuário solicitar a saída do programa.

""" 
Apenas para somar, subtrair, multiplicar ou dividir apenas dois números	

	
"""


num_1 = input('Digite o primeiro número: ')
num_2 = input('Digite o segundo número: ')
operador = input('Digite o operador: ')

try:
  num_1 = int(num_1)
  num_2 = int(num_2)
  if operador == "+":
    resultado = num_1 + num_2
  elif operador == "-":
    resultado = num_1 - num_2  
  elif operador == "*":
    resultado = num_1 * num_2
  elif operador == "//":
    resultado = num_1 // num_2   
  print(f'O resultado da calculadora é {resultado}.')
except:
  print('Houve algum erro de digitação. Forneça apenas os números e'
    ' o operador.')
