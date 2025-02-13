# aula 206b

"""
Crie um classe. Salve os dados dela em um arquivo json.
Depois, leia o arquivo json que você criou e passe os dados
para outro arquivo python
"""

# Este arquivo importará a classe e os dados de um json

import json
from aula206a_salvando_dados_de_classe_em_json import DIRETORIO_DO_NOVO_ARQUIVO, Carro, toro

with open(DIRETORIO_DO_NOVO_ARQUIVO, 'r') as json_file:
    dados_importados_json = json.load(json_file)
# As instâncias não são importadas junto com a classe 
# portanto elas devem ser recriadas ou importadas explicita-
# mente, isto é, uma por vez
    compass = Carro(**dados_importados_json[0])

for dado in dados_importados_json:
    print(dado)

print(f'\nA marca da {compass.nome} é {compass.marca}.')
print(f'\nA marca da {toro.nome} é {toro.marca}.\n')
    
