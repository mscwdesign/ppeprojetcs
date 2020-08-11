"""
Reduce

OBS a partir do python 3+ a func 'reduce()' não é mais built-in
Agora temos que importar e utilizar esta função a partir do modulo functools

# imagine que você tem uma coleção de dados

dados = [a1, a2, a3]

# e vc tem uma função q recebe 2 parametros

def funcao(x, y):
    return x * y

Assim como map() e filter() a func reduce() recebe dois parametros: a func e o iteravel

reduce(funcao, dados)

a função reduce() funciona da seguinte forma
    Passo 1: res1 = f(a1, a2) # aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res

    isso é repetido até o final
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(resn, an)

ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final
reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a função reduce() como:

fucao(funcao(funcao(a1, a2,), a3), a4), ...), an)

"""

# Exemplo

from functools import reduce

dados = [1, 2, 3, 4, 5, 6, 7]

# para utilizar o reduce() precisamos de uma func que receba 2 parametros

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando loop normal

res = 1
for n in dados:
    res = res * n

print(res)