"""
Por padrão, Python não sabe como deve organizar os dicionários, portanto devemos
dizer a ele que "regras" ele deve usar para organiza-los. No caso abaixo, dissemos
a ele para organizar pelas chaves 'Nome'. Fornecemos a ele todas essas chaves e ele
as organiza.
"""

lista = [
    {'Nome': 'Lucas'},
    {'Nome': 'Pedro'},
    {'Nome': 'João'},
    {'Nome': 'Ana Maria'},
    {'Nome': 'Letícia'},
    {'Nome': 'Diego'},
    {'Nome': 'Carol'},
    {'Nome': 'Rita'},
]

def ordenar(dicionario):
    return dicionario['Nome']

lista.sort(key=ordenar)

for dicionario in lista:
    print(dicionario)