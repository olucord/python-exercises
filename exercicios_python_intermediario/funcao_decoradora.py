def executa(funcao): # função decoradora
    def executa2(*args):
        print('Fiz algo antes da execução da função')      
        resultado = funcao(*args)
        print(resultado)
        print('Fiz algo depois da execução da função', end='\n\n')      
        return 
    return executa2

@executa # decorador
def inverte_string(string):
    return string[::-1]

# Se fosse manualmente, seria assim:
# primeira_chamada = executa(inverte_string) # = executa2
# primeira_chamada('Lucas')

inverte_string('Lucas')
print(inverte_string.__name__) # mão é mais 
# invert_string, mas sim executa 2
