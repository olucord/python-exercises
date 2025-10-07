# Manipulando caminhos

import pathlib

# criando objeto PosixPath
DIRETORIO = pathlib.Path('folder-example')
print(f'A pasta checada é a "{DIRETORIO}"\n')


# checando os arquivos dessa pasta -> retorna um GENERATOR, então
# vamos converter para LIST para podermos reutilizar os dados
arquivos_da_pasta = list(DIRETORIO.glob('*')) 
print('arquivos_da_pasta\n') 

for arquivo in arquivos_da_pasta:
    print(arquivo)

print(f'{50*'-'}')

# checando todos os arquivos (recursão) dessa pasta -> retorna um GENERATOR, 
# então vamos converter para LIST para podermos reutilizar os dados

todos_arquivos_da_pasta = list(DIRETORIO.rglob('*')) 
print('todos_arquivos_da_pasta\n') 

for arquivo in todos_arquivos_da_pasta:
    print(arquivo)

print(f'{50*'-'}')

# checando arquivos com tipos específicos
arquivos_xlsx = list(DIRETORIO.rglob('*.xlsx')) 
print('todos_arquivos_da_pasta\n') 

for arquivo in todos_arquivos_da_pasta:
    print(arquivo)

print(f'{50*'-'}')

# checando arquivos com nomes específicos
arquivos_xlsx = list(DIRETORIO.rglob('arquivo*.xlsx')) 
print('todos_arquivos_da_pasta\n') 

for arquivo in todos_arquivos_da_pasta:
    print(arquivo)


