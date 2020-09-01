"""
Entendendo iterators e iterables

iterator -> um objeto que pode ter iterado.
            um objeto que retorna um dado, sendo um elemento por vez quando uma func next() é chamada

Iterable ->
    um objeto que ira retornar um iterator quando a função iter() for chamada


python = 'Hello World'
numeros = [1, 2, 3, 4]

it1 = iter(nome)
it2 = iter(numeros)


print(next(it1))
"""

python = 'Hello World'

for letra in python:
    print(f'{letra}')