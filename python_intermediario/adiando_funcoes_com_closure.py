def soma(x,y):
    return x + y

# def executa(funcao, *args):
#     return funcao(*args)

# Queremos que o valor que eu passar depois some 5
# somar_cinco = executa(soma, 5) # gera erro

# Para contornar

def executa2(funcao, x):
    def executa3(y):
        return funcao(x, y)
    return executa3

# Agora consigo chamar depois e somar com 5

somar_cinco = executa2(soma, 5) # soma_cinco 
# recebeu o valor de retorno, ou seja, 
# somar_cinco = executa3 

print(somar_cinco(10)) # mesmo que executa(10)


