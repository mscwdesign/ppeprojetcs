"""
Modulos integrados que já vem instalado no python

|Python|Modulos builtin|

#Utilizando Alias(apelidos para modulos)
import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *

print(random())


from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())
"""

# Costumamos utilizar tuple  para colocar multiplos importts de um mesmo modulo

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(3, 10))
lista = [1, 2]
shuffle(lista)
print(lista)
print(choice('Python'))
