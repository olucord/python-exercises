# aula 192
"""
Crie uma lista de tarefas que permita adicionar os itens, 
desfazer ou refazer (isto é os itens adicionados). 
"""

# Adicionei uma pequena funcionalidade. Sempre que o usuário digita um 
# novo item, a lista de refazer será sobrescrita. Alguns aplicativos 
# dispõem desse mecanismo para evitar confusões na ordem das ações.

from os import system # importando system para limpar o terminal

# Primeiro criamos listas para armazenar os dados
tarefas = []
refazer = []

def exibir_tarefas():
    system('cls') # de {os}
    print('SUAS TAREFAS:')
    for tarefa in tarefas:
        print(f'• {tarefa}')
    print('')

def adicionar_na_lista(lista, valor):
  lista.append(valor)

def remover_ultimo_item_da_lista(lista):
  del lista[-1]

# Aqui tive que passar também uma string com o nome da lista, para 
# evitar referências indesejadas de parâmetros mutáveis, como é o 
# caso de listas

def checando_se_a_lista_esta_vazia(lista, nome_da_lista):
  if len(lista) == 0:
    exibir_tarefas()
    if nome_da_lista == 'tarefas': # lista de tarefas sem itens a desfazer
      print('\nNão há nada para desfazer\n')
    else: # lista de refazer sem itens a refazer
      print('\nNão há nada para refazer\n')
    return True
  return False

# return "True" ou "False" funcionará como uma flag para saber se 
# o "continue" irá ser ativado ou não dentro do "while", podendo 
# assim, reiniciar o loop
 
while True:
  print('[D]esfazer [R]efazer [S]air')
  entrada = input('Adicione uma tarefa: ').strip()

  if not entrada: # verifica se a entrada está vazia
    exibir_tarefas()
    print('\nVocê precisa digitar alguma coisa\n')
    continue

  if entrada.lower() == 'd': # tentando desfazer a última ação
    if checando_se_a_lista_esta_vazia(tarefas, 'tarefas'):
      continue
    adicionar_na_lista(refazer, tarefas[-1])
    remover_ultimo_item_da_lista(tarefas)
    exibir_tarefas()

  elif entrada.lower() == 'r': # tentando refazer a última ação
    if checando_se_a_lista_esta_vazia(refazer, 'refazer'):
      continue
    adicionar_na_lista(tarefas, refazer[-1])
    remover_ultimo_item_da_lista(refazer)
    exibir_tarefas()

  elif entrada.lower() == 's': # saindo do programa
    exibir_tarefas()
    break

  else: # nenhuma das opções anteriores, então adiciona a tarefa
    if len(tarefas) >= 0: 
      refazer.clear() # Ao gerar um novo item, a lista 
# de refazer será limpada para evitar conflito de ordem 
# com os novos elementos
    adicionar_na_lista(tarefas, entrada)
    exibir_tarefas()
