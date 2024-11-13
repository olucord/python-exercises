"""
Senhas muito grandes, a proporção colocada pode causar confusão. Não colocar
senhas maiores que 50, por exemplo.
"""

from random import sample # número aleatórios em um intervalo
from os import system # permite usar códigos do terminal

# Caracteres
letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 20% da senha
letras_minusculas = 'abcdefghijklmnopqrstuvwxyz' # 20% da senha
numeros = '0123456789' # 20% da senha
simbolos = '+-*/~^&%$#@!?.>,;:<()_}[]{' # 40% da senha

# Definindo tamanho da senha
tamanho_da_senha = 50

conjunto_vazio = set()

def adicionar_caractere(grupo, porcentagem):
    try:    
        for i in sample(grupo, round(porcentagem*tamanho_da_senha)):
            conjunto_vazio.add(i) 
    except:
        None        

adicionar_caractere(letras_maiusculas, 0.2)
adicionar_caractere(letras_minusculas, 0.2)
adicionar_caractere(numeros, 0.2)
adicionar_caractere(simbolos, 0.4)
print(conjunto_vazio)

# Criando a senha           
senha = ''

for i in conjunto_vazio:
    senha += i

system('cls')
print(f'Ok. Aqui está uma senha de {tamanho_da_senha} caracteres:')
print(senha)
