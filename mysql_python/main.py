import pymysql # vai permitir conectar o Python
# com a base de dados no servidor MySQL
# e manipulá-la pelo Python
import dotenv # serve para importar as variáveis de 
# ambiente do arquivo ".env" diretamente para o nosso
# código Python
import os

dotenv.load_dotenv() # referencia as variáveis de 
# ambiente com o módulo os usando o método "environ[V.A]"

TABLE_NAME = 'customers'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

# com o "os.environ['chave']" evitamos de subir dados
# sensíveis (informações pessoais) diretamente no
# código. Elas ficam salvas em um arquivo local que 
# não é enviado para a nuvem (outras pessoas não tem 
# acesso) que é o .env (environment)

# cursor = connection.cursor()

# # SQL

# print('O código funcionou. O cursor está em:', cursor)

# cursor.close()
# connection.close()

#********************************************************
# Alternativa de código
#********************************************************

# with connection:  
#     with connection.cursor() as cursor:
#         cursor.execute( # Código SQL
#             'CREATE TABLE IF NOT EXISTS customers ('
#             'id INT NOT NULL AUTO_INCREMENT, '
#             'name VARCHAR(50) NOT NULL, '
#             'age INT NOT NULL, '
#             'PRIMARY KEY (id) '
#             ') '
#         )
        # print(f'O código funcionou. O cursor está em "{cursor}"')

cursor = connection.cursor()

# cursor.execute(
#     f'CREATE TABLE buyers ('
#     'id INT NOT NULL AUTO_INCREMENT, '
#     'name TEXT NOT NULL, '
#     'phone INT NOT NULL,'
#     'city TEXT NOT NULL, '
#     'PRIMARY KEY (id) '
#     ')'             
# )

# cursor.execute(
#     f'CREATE TABLE cars ('
#     'id INT NOT NULL AUTO_INCREMENT, '
#     'name TEXT NOT NULL, '
#     'mark TEXT NOT NULL, '
#     'year INT NOT NULL, '
#     'color TEXT NOT NULL, '
#     'PRIMARY KEY (id) '
#     ')'             
# )

cursor.execute(
    'INSERT INTO buyers '
    '(name, phone, city) ' 
    'VALUES ("Vinicius", 990909192, "Recife"), '
    '("Carol", 990909193, "Camaragibe"), '
    '("Pedro", 990909194, "João Pessoa") '
)

cursor.execute(
    'INSERT INTO cars '
    '(name, mark, year, color) ' 
    'VALUES ("Compass", "Jeep", 2018, "White Pearl"), '
    '("Toro", "Fiat", 2021, "Black"), '
    '("Renegade", "Jeep", 2021, "Black") '
)


connection.commit()
print('Salvando')

cursor.close()
connection.close()