# aula 103, exemplo

"""
Criando um gerador de cpf válido pelas regras do GOV.BR
"""

import os
import random

while True:
    escolha = input('Digite "g" para gerar um cpf (ou "s" para sair do programa): ')
    if escolha == "g":
        Nove_primeiros_caracteres = ''
        for i in range(0,9,1):
            Nove_primeiros_caracteres += str(random.randint(0,9))
            

        regressao1 = range(10,1,-1)
        soma_e_multiplicacao = 0
        for i in range(0,9,1):
            soma_e_multiplicacao += int(Nove_primeiros_caracteres[i]) * regressao1[i]
        resultado = ((soma_e_multiplicacao*10)%11)
        primeiro_digito = resultado if resultado <= 9 else 0

        Nove_primeiros_caracteres = Nove_primeiros_caracteres + str(primeiro_digito)
        regressao2 = range(11,1,-1)
        soma_e_multiplicacao = 0
        for i in range(0,10,1):
            soma_e_multiplicacao += int(Nove_primeiros_caracteres[i]) * regressao2[i]
        resultado = ((soma_e_multiplicacao*10)%11)
        segundo_digito = resultado if resultado <= 9 else 0
        os.system('cls')
        print(f'O CPF gerado é {Nove_primeiros_caracteres[:3]}.\
{Nove_primeiros_caracteres[3:6]}.{Nove_primeiros_caracteres[6:9]}-\
{primeiro_digito}{segundo_digito}.')
    elif escolha == "s":
        os.system('cls')
        break
    else:
        os.system('cls')
        print('Por favor, escolha uma das opções abaixo.')   