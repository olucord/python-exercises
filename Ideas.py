

def decorador_diz_ola(func):
    def intern(*args, **kwargs):
        print('Eu adicionei um comportamento novo na função')
        return func(*args, **kwargs)
    return intern    

@decorador_diz_ola
def somar(x, y):
    return x + y

print(somar(5,4))