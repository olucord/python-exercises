# aula 124
# cada dicionário é formado por pares de chave-valor
# escreva a solução escrita antes e depois transforme-a em código pela lógica😊
"""
Código mais simples é melhor que complexo. O código abaixo poderia ser mais simples
usando Flags, para controlar o fluxo do código (no tratamento da resposta), poderia
simplesmente ter usado um "acerto = False" e quando "acerto = True", exibir a msg...
Usamos uma condição bem complexa em "if int(escolha) == ..."(complexo)
"""
"""
Crie um sistema de perguntas e respostas (assunto mais ressente aprendido -> dicionários)
"""

perguntas = {
1 : {'Pergunta':'Qual era o nome do apóstolo Pedro, antes de jesus \
lhe dar esse nome?', 'Alternativas': ['Simão', 'Maciel', 'Felipe', 'Jordão'],\
'Resposta':'Simão'},
2 : {'Pergunta':'Qual era o nome do gigante que Davi derrubou?','Alternativas':['Barrabás',\
'Golias','Anaque', 'Barnabé'], 'Resposta':'Golias'},
3 : {'Pergunta':'Quantos animais foram colocados na arca de Noé?', 'Alternativas':[\
'Um casal de cada espécie','Só animais machos', 'Um filhote de cada espécie'],\
'Resposta':'Um casal de cada espécie'}
}

print('Analise as perguntas abaixo e escolha a opção correta: ', end='\n\n')
acerto = 0

def pergunta(chave_atual): # chave atual é o nº da pergunta na lista
    # exibindo pergunta e número da pergunta
    print(f'{list(perguntas.keys())[chave_atual-1]} - {perguntas[chave_atual]['Pergunta']}')
    # exibindo alternativas
    for i, alternativa in enumerate(perguntas[chave_atual]['Alternativas']):
        print(f'({i+1}) {alternativa}')
    escolha = input('Qual a a alternativa correta? ')
    # tratamento da resposta (se o número respondido corresponde ao indice da resposta)
    if int(escolha) == (perguntas[chave_atual]['Alternativas'].index(perguntas[chave_atual]['Resposta'])+1):
        print('Você acertou✨🎉', end='\n\n')
        global acerto
        acerto += 1
    else:
        print('Você errou❌', end='\n\n')
    return

while True:
    pergunta(1)
    pergunta(2)
    pergunta(3)
    print(f'Você acertou {acerto} de {len(perguntas)}.')
    break