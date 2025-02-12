import sqlite3
from criando_base_de_dados import DATA_BASE, TABLE_NAME

connection = sqlite3.connect(DATA_BASE)
cursor = connection.cursor()

# cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id BETWEEN "11" AND "46"')

cursor.execute(f'DELETE FROM {TABLE_NAME} ' 
' WHERE height="28.32"')

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    print(row)

connection.commit()

cursor.close()
connection.close()
