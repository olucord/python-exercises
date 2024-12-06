from random import sample

caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012345\
6789+-*/~^&%$#@!?.>,;:<()_}[]{'

senha = ''

for i in sample(caracteres, 88): # o máximo são 88 caracteres
    senha += i

print(senha)
