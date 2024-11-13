# Um decorador não substitui o valor do decorador 
# anterior, mas atualiza-o. Por isso, "final" no 
# código abaixo não é sobrescrevido, mas sim con-
# catenado entre os dois decoradores

def parametros_do_decorador(nome):
    def decorador(funcao):
        def modificacoes_do_decorador(*args, **kwargs):
            res = funcao(*args, **kwargs)   
            final = f'{res} {nome}'
            return final
        return modificacoes_do_decorador
    return decorador

@parametros_do_decorador('Segundo')
@parametros_do_decorador('Primeiro')
def soma(x, y):
    return x + y

a = soma(10,5)
print(a)