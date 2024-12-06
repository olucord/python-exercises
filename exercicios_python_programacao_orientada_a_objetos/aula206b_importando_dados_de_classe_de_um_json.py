# aula 206b

"""
Crie um classe. Salve os dados dela em um arquivo json.
Depois, leia o arquivo json que você criou e passe os dados
para outro arquivo python
"""

# Este arquivo importará a classe e os dados de um json

dados_importados_json = None

import json
from aula206a_salvando_dados_de_classe_em_json import DIRETORIO_DO_NOVO_ARQUIVO

with open(DIRETORIO_DO_NOVO_ARQUIVO, 'r') as json_file:
    dados_importados_json = json.load(json_file)

for dado in dados_importados_json:
    print(dado)
    