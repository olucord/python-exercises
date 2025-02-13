import pymysql # vai permitir conectar o Python
# com a base de dados no servidor MySQL
# e manipulá-la pelo Python
import dotenv # serve para importar as variáveis de 
# ambiente do arquivo ".env" diretamente para o nosso
# código Python
import os

dotenv.load_dotenv() # referencia as variáveis de 
# ambiente com o módulo os usando o método "environ[V.A]"

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

cursor = connection.cursor()

# SQL

print('O código funcionou', cursor)

cursor.close()
connection.close()
