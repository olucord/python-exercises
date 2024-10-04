# aula 54

"""
Mostrando diversos valores
"""

num = input("Digite um número inteiro: ")

try:
    num = int(num)
    if num % 2 == 0:
        print(f"Seu número inteiro é o {num} e ele é par.")
    else:
        print(f"Seu número inteiro é o {num} e ele é ímpar.")
except:
    print("Isso que você digitou não é um número inteiro!")

################################################################

hora = input("Digite a hora atual: ")

try:
  hora = int(hora)
  if hora >= 0 and hora <= 11:
    print("Bom dia!")
  elif hora >= 12 and hora <= 17:
    print("Boa tarde!")
  elif hora >= 18 and hora <= 23:
    print("Boa noite!")
  else:
    print("Digite uma hora válida entre 0 e 23 horas.")
except:
  print("Digite uma hora válida entre 0 e 23 horas.")


################################################################


nome = input("Digite seu primeiro nome: ")

quant_letras = len(nome)

if nome:
  if quant_letras <= 4: 
    print("Seu nome é curto.")
  elif quant_letras >= 5 and quant_letras <= 6: 
    print("Seu nome é normal.")
  else: 
    print("Seu nome é muito grande.")   
else:
  print("Parece que você não digitou nada.")    

