from os import system

tarefas = []
refazer = []

def exibir_tarefas():
    system('cls')
    print('SUAS TAREFAS:')
    for tarefa in tarefas:
        print(f'• {tarefa}')
    print()

def verificar_se_a_lista_esta_vazia(lista, nome_da_lista):
    if len(lista) == 0:
        exibir_tarefas()
        if nome_da_lista == 'tarefas': # tarefas vazia = sem itens a desfazer
            print('\nNão há itens a desfazer\n')
        else: # nome_da_lista == 'refazer': - refazer vazio = sem itens a refazer
            print('\nNão há itens a refazer\n')
        return True
    return False

# Para evitar o uso de condicionais
def func_desfazer(item):
    if verificar_se_a_lista_esta_vazia(tarefas, 'tarefas'):
        return
    refazer.append(tarefas[-1])
    del tarefas[-1]
    exibir_tarefas()
    
def func_refazer(item):
    if verificar_se_a_lista_esta_vazia(refazer, 'refazer'):
        return
    tarefas.append(refazer[-1])
    del refazer[-1]
    exibir_tarefas()

def adicionar(item):
    refazer.clear()
    tarefas.append(item)
    exibir_tarefas()

while True:
    print('[D]esfazer - [R]efazer:')
    entrada = input('Adicione uma terefa: ').lower()

    comandos = {
        'd': lambda: func_desfazer(entrada),
        'r': lambda: func_refazer(entrada),
        'adicionar': lambda: adicionar(entrada)
    }

    comando = comandos.get(entrada) if comandos.get(entrada) \
        is not None else comandos['adicionar']

    comando()