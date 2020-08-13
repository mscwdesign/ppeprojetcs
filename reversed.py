"""
Reversed

obs: não confunda com a função reverse() que estudamos nas listas

a função reverse só funciona com lista

a função reversed funciona com qlqr iteravel

a função reversed() retorna um iteravel chamado List Reverse Iterator

"""

lista = [1, 2, 3]

res = reversed(lista)

print(res)
print(type(res))

print(list(reversed(lista)))

print(tuple(reversed(lista)))

print(set(reversed(lista)))

for letra in reversed('Python'):
    print(letra, end='')

print('\n')

print(''.join(list(reversed('Python'))))

for n in reversed(range(0, 10)):
    print(n)

for n in range(9, -1, -1):
    print(n)
