"""
Funções de Maior Grandeza - High Order Functions - HOF


- Quando uma linguagem de programação suporta HOF indica que podemos ter funções
que retonram outras funções como resultado, ou mesmo podemos passar funções como argumentos
para outras funções, até mesmo criar variaveis do tipo de funções nos nossos programas.

OBS na seção de funções nos usamos isso


Em python, as funções são cidadões de primeira classe, First Class Person

# Exemplos

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return  a * b

def dividir(a, b):
    return  a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

# Nested Functions

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto de você '))
    return humor() + pessoa

print(cumprimento('Angelina'))


# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahaahahaha', 'kkkkkkkkkkkkk', 'yayayayayaayyaya'))
    return rir()

rindo = faz_me_rir()
print(rindo)
"""

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahhahahahah', 'kkkkkkkkkk', 'hihihihihihih'))
        return f'{risada} {pessoa}'
    return dando_risada

rindo = faz_me_rir_novamente('Fernanda ')

print(rindo())
