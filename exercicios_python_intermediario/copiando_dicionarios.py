import copy

def volta_na_copia_certa(): # corrige um exemplo mostrado
    global copia_isolada_de_dicionario
    copia_isolada_de_dicionario = [
    {**dic,'Idade':dic['Idade']+15}
    for dic in meus_dados
]
    

meus_dados = [
    {
        'Nome':'Lucas',
        'Idade':25,
        'Curso':'Engenharia'
    },
    {
        'Nome':'Ayanne',
        'Idade':30,
        'Curso':'Odontologia'
    }

]

copia_profunda_dos_meus_dados = copy.deepcopy(meus_dados)

# Também é possível copiar lista de dicionários assim:

copia_isolada_de_dicionario = [
    {**dic,'Idade':dic['Idade']+15}
    for dic in meus_dados
]

"""
O CASO ABAIXO também copia uma lista independente, 
porém os *dicionários não*, eles seriam referenciados
ALTERANDO OS DADOS PRINCIPAIS!!!
""" 
copia_isolada_de_dicionario = [
    dic # , 'Idade':dic['Idade']+15 -> não pega mais
    for dic in meus_dados
]

volta_na_copia_certa()

# copia_isolada_de_dicionario[0]['Nome'] = 'Carlos'

print(*meus_dados, sep='\n')
print()
print(*copia_isolada_de_dicionario, sep='\n')
