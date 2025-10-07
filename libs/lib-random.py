import random

numeros = [1,2,3,4,5,6,7,8,9]
print(numeros)

# controle de aleatoriedade e reprodibilidade
random.seed(a=None)
# podemos trocar para alguma valor para sempre reproduzir
# os mesmos números aleatórios. Tipo random.seed(42) 
# sempre retorna os mesmos valores

# mistura os valores
random.shuffle(numeros)
print(f'{numeros} - shuffle - tipo {type(numeros)}')


# escolher uma certa quantidade de valores aleatórios de uma sequência 
sampled = random.sample(numeros, 3)
print(f'{sampled} - sample - tipo {type(sampled)}')

# número flutuante aleatório entre 0 e 1
aleatorio = random.random()
print(f'{aleatorio} - random - tipo {type(aleatorio)}')

# número inteiro aleatório entre dois valores
aleatorio_int = random.randint(0, 10)
print(f'{aleatorio_int} - randint - tipo {type(aleatorio_int)}')

# número inteiro aleatório entre dois valores, mas estabelecendo passo
aleatorio_int2 = random.randrange(0,10,2)
print(aleatorio_int2)

# escolhe um valor aleatório de uma sequência
random_value = random.choice(numeros)
print(random_value)

# escolhe um número de ponto flutuante aleatório entre um intervalo
random_float = random.uniform(0, 5)
print(random_float)

# Retorna um valor aleatório de uma distribuição Gaussiana (ou normal). 
# Os parâmetros mu (média) e sigma (desvio padrão) definem a forma da
#  curva de sino. Esta é uma das distribuições mais importantes na 
# estatística e é fundamental para simulações em física, engenharia 
# e finanças.
# random.gauss(mu, sigma) 

# Retorna um valor de uma distribuição 
# exponencial. É frequentemente utilizada para modelar o tempo entre 
# eventos, como o tempo entre chegadas de clientes em uma fila ou o 
# tempo de vida de um componente eletrônico.
# random.expovariate(lambd)