# aula 98 
"""
Crie um algoritmo para validação de cpf, segundo as intruções do GOV.BR
"""

cpf = '649.340.175-50'
# Primeira parte do código (Dígito 1)
lista_num_do_cpf_checagem = []
contagem_regressiva = range(10,1,-1) # sequência num para * na checagem
# obtendo a lista com os números para checar o dígito 1
for num in cpf:
    if len(lista_num_do_cpf_checagem) == 9:
        break
    if num != '.':
        lista_num_do_cpf_checagem.append(int(num))
    else:
        None
# somando os números assim que multiplica-los
soma_dos_num_multiplicados = 0
for i in range(0,9,1): # range para os índices
    multiplicacao = lista_num_do_cpf_checagem[i]*contagem_regressiva[i]
    soma_dos_num_multiplicados += multiplicacao # melhor seria -> soma_dos_num_multiplicados += lista_num_do_cpf_checagem[i]*contagem_regressiva[i]
# multiplicar o resultado anterior por 10
resultado_x_dez = soma_dos_num_multiplicados * 10
# obter o resto da divisão do resultado anterior por 11
resultado_resto_divisao_por_11 = resultado_x_dez % 11
if resultado_resto_divisao_por_11 > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resultado_resto_divisao_por_11
print(f'O primeiro dígito é {primeiro_digito}')

# Segunda parte do código - (Dígito 2) - basicamente uma cópia da primeira parte, pouco alterada
lista_num_do_cpf_checagem = []
contagem_regressiva = range(11,1,-1) # sequência num para * na checagem
# obtendo a lista com os números para checar o dígito 2
for num in cpf:
    if len(lista_num_do_cpf_checagem) == 10:
        break
    if num.isdigit():
        lista_num_do_cpf_checagem.append(int(num))
    else:
        None

soma_dos_num_multiplicados = 0
for i in range(0,10,1): # range para os índices
    soma_dos_num_multiplicados += lista_num_do_cpf_checagem[i]*contagem_regressiva[i]
resultado = ((soma_dos_num_multiplicados*10)%11)
segundo_digito = 0 if resultado > 9 else resultado

print(f'O segundo dígito é {segundo_digito}')

if str(primeiro_digito) == cpf[12] and str(segundo_digito) == cpf[13]:
    print('O CPF inserido é válido segundo o GOV.BR')
else:
    print('O CPF inserido não é válido segundo o GOV.BR')
