# aula 194

"""
Salve a lista de tarefas do exercício anterior (aula 192) 
em formato json. 
"""

# Primeiro, vamos importar o módulo py onde fiz a lista de tarefas
import aula192_criando_lista_de_tarefas

# Se executarmos até aqui, funciona tudo normal, assim como 
# no código anterior, afinal importei tudo (comentando o 
# resto abaixo)

from sys import exit

while True:
    pergunta = input('Você gostaria de salvar as tarefas\
 em json? (S/N)').lower().strip()

    if pergunta == 's' or pergunta == 'sim':
        break
    elif pergunta == 'n' or pergunta == 'não':
        exit()
    else:
        print('\nVocê precisa responde "sim" ou "não"')

import json
import os

# Local onde irei salvar o arquivo .json
diretorio_que_contem_este_arquivo = os.path.dirname(__file__)
# Se quisessemos o caminho completo do arquivo 
# bastava pegar diretamente a variável "__file__"

# Unindo, de modo formatado (isto é, com compatibilidade 
# com qualquer sistema operacional) o diretorio que contém o 
# arquivo atual e o nome do novo arquivo, criando assim, o 
# caminho do novo arquivo completamente 
caminho_do_novo_arquivo_json = os.path.join(diretorio_que_contem_este_arquivo, 'tasks_list_json_file.json')

# Dados a serem importados estão em "tarefas da aula 192" (uma lista)
with open(caminho_do_novo_arquivo_json, 'w', encoding='utf8') as json_file:
    json.dump(
        aula192_criando_lista_de_tarefas.tarefas, 
        json_file,
        indent=2,
        )








