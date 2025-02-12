import sqlite3
import pathlib

# Escrevendo em inglês para acostumar
PATH_FOLDER_OF_ARCHIVE = pathlib.Path(__file__).parent
NAME_OF_DATA_BASE = 'minha_base_sqlite'
DATA_BASE = PATH_FOLDER_OF_ARCHIVE / NAME_OF_DATA_BASE
TABLE_NAME = 'persons'

# print(DATA_BASE)

# *CONNECTION* conexão do código Python com o banco de dados
connection = sqlite3.connect(DATA_BASE)
# *CURSOR* permite passar comandos SQL para o banco de dados
cursor = connection.cursor()

# código SQL
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}\
    (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, height REAL)'
    )

# Salvando a tabela
connection.commit()

# Apagando todos os dados da tabela
# cursor.execute(f'DELETE FROM {TABLE_NAME}')
# cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')

# Colocando dados na tabela
# sql_code = (f'INSERT INTO {TABLE_NAME} (name, height)'
# 'VALUES (:nome, :altura)')

# entrada_usuario = [{"nome": "Merlin", "altura" : 16.4},
# {"nome": "Coda", "altura" : 28.32}, 
# {"nome": "Barack", "altura" : 100.8},
# {"nome": "Smith", "altura" : 100.8}]

# cursor.executemany(sql_code, entrada_usuario)

connection.commit()

cursor.close()
connection.close()

if __name__ == '__main__':
    print('Cursor fechado com sucesso')
    print('Connection fechado com sucesso')