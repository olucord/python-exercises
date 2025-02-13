# aula 76
# O professor fez um código mais simples. Segue abaixo do meu.

""" 
Tem que acertar a palavra secreta, digitando e revelando as letras em "*********"	
"""

palavra_secreta = 'macarrao'
letras_secretas = '*'*len(palavra_secreta)
nova_palavra_secreta = '*'*len(palavra_secreta)
sair_do_jogo = False
print(letras_secretas)
letra_digitada = input('Digite uma letra: ')
tentativas = 0

"""
letra_atual é a variável para saber onde é a posição certa para 
revelar a letra digitada que está contida na palavra secreta
"""

while True: 

  tentativas += 1
  
  if letra_digitada in palavra_secreta:
      
      for letra_atual in palavra_secreta:
        
        if letra_digitada == letra_atual:
          
          indice_procurado = palavra_secreta.find(letra_atual)
          nova_palavra_secreta = letras_secretas[:indice_procurado] + letra_atual + letras_secretas[indice_procurado + 1:]
          letras_secretas = nova_palavra_secreta
          palavra_secreta = palavra_secreta[:indice_procurado] + '*' + palavra_secreta[indice_procurado+1:]
          if '*' not in nova_palavra_secreta:
            print('Parabéns você conseguiu!')
            print(f'A palavra era macarrao.')
            print(f'Tentativas {tentativas}')
            sair_do_jogo = True
            
      else:
        if sair_do_jogo:
          break    
        print(nova_palavra_secreta)
        letra_digitada = input('Digite outra letra: ')  
  else:
    print(nova_palavra_secreta)
    letra_digitada = input('Digite outra letra: ')
    continue 

#################################### código do professor #############################################

"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0