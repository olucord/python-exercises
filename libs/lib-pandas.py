import pandas as pd

# DataFrame simula uma tabela -> várias colunas
# Series simula uma série -> uma única coluna

# criando um DataFrame na hora
new_df = pd.DataFrame({
    'nome':['Lucas', 'Maria', 'João', 'Luiza'], 
    'idade':[18, 32, 26, 22], 
    'curso':['MA', 'DS', None, 'DS'], 
    })

print(new_df)

# criando um DataFrame a partir de algum arquivo csv, xls...
df = pd.read_csv('Titanic-Dataset.csv')

# pegando informações do arquivo
print(df.info())

# resumo estatístico (contagem, média, desvio padrão, quartis, max, mín)
print(df.describe())

# número de linhas e colunas
print(df.shape)

# primeiras cinco e últimas cinco linhas (podemos passar a quantidade)
print(df.head(8))
print(df.tail(8))

# vendo coluna ou colunas de um df
print(new_df['nome']) # cria series
print(new_df[['nome', 'curso']]) # cria dataframe

# valor de uma coluna
print(new_df['nome'].iloc[0])
print(new_df['nome'].head(2))

# pegando dados por rótulo
print(new_df.loc[0])

# # pegando dados por índice
print(new_df.iloc[0])

# pegando dados por linha e coluna (linha 0 e coluna 1)
print(new_df.iloc[0, 1])

# especificando a linha e as colunas
print(new_df.iloc[0, [0, 2]])

# pegando dados de várias linhas e várias colunas
print(new_df.loc[0:1, ['nome', 'idade']])

# pegando valores únicos de uma coluna
print(new_df['nome'].unique())

# pesquisa filtrada com base nos valores
print(new_df[new_df['idade']>20])

# pesquisa filtrada com base em vários valores
print(new_df[(new_df['idade']>20) & (new_df['idade']<30)])

# valores ausentes em boolean (true para ausente e false para existente)
print(new_df.isnull())

# visualizar sem valores ausentes (tira a linha toda)
print(new_df.dropna())

# apagando valores específicos
print(new_df.drop('curso', axis=1)) # axis = 1 -> coluna / axis = 0 -> linha

# removendo linhas com valores ausentes
print(new_df.dropna(inplace=True))

# preencher com médias, medianas, modas, etc
print(new_df.ffill())

# removendo duplicatas
print(new_df.drop_duplicates())

# agrupando por alguma coluna e realizando alguma operação em outra
# agrupando por curso e somando idades
print(new_df.groupby('curso')['idade'].mean())

# renomeando colunas
# df.columns = [
# 	'coluna1',
# 	'coluna2',
# 	'coluna3',
# 	'coluna4'
# ] -> para redefinir todos os nomes das colunas
# 
# ou 
# 
# podemos usar df.columns = lista_com_novos_nomes_colunas

# df.rename(columns={
# 	'nome_antigo':'novo_nome', 
# 	'nome_antigo2':'novo_nome2'
# }) -> para renomear colunas específicas

# alterando nomes dos índices
# new_df = df.rename(index={0:'Primeiro valor', 1:'Segundo valor'}) -> 
# cria uma cópia temporária
# 
# or
#
# df = df.rename(index={0:'Primeiro valor'}, inplace=True) -> para 
# alterar o orignal

print(f'{100*'*'}')

# consultas nos dados
print(new_df.query('idade > 20'))
