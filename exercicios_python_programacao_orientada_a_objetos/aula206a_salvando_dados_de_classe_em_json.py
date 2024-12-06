# aula 206a

"""
Crie um classe. Salve os dados dela em um arquivo json.
Depois, leia o arquivo json que você criou e passe os dados
para outro arquivo python
"""

# Este arquivo conterá a classe e os dados a serem exportados
# para json

class Carro():
    def __init__(self, nome, marca, ano, cor):
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.cor = cor

compass = Carro('Compass', 'Jeep', 2018, 'Branco Pérola')
renegade = Carro('Renegade', 'Jeep', 2021, 'Preta')
toro = Carro('Toro', 'Fiat', 2021, 'Preta')

lista_dicionarios_instancias = [compass.__dict__,\
     renegade.__dict__,toro.__dict__]

# print(lista_dicionarios_instancias)

import os
import json

DIRETORIO_QUE_CONTEM_ESTE_ARQUIVO = os.path.dirname(__file__)
DIRETORIO_DO_NOVO_ARQUIVO = os.path.join(DIRETORIO_QUE_CONTEM_ESTE_ARQUIVO, 'dados_da_classe_carro.json')

with open(DIRETORIO_DO_NOVO_ARQUIVO, 'w', encoding='utf8') as json_file:
    json.dump(
        lista_dicionarios_instancias,
        json_file,
        indent=2
    )


