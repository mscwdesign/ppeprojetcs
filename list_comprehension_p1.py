"""
List Comprehension

Utilizando list comprehension nos podemos gerar novas listas com dados processados a partir de outro
iteravel.

# Sintax

[ dado for dado in iteravel ]


lista = [1, 2, 3]

res = [numero *10 for numero in lista]
print(res)

# Expressão em 2 partes
# 1 For numeros in numeros
# 2 numero * 10

res = [numero / 2 for numero in lista]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in lista]
print(res)

# List Comprehension VS Loop

# Loop

numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in numeros])


"""

# Outros Exemplos

# 1

nome = 'Python'

print([letra.upper() for letra in nome])

# 2

def caixa_alta(amigos):
    nome = amigos.replace(amigos[0], amigos[0].upper())
    return nome

amigos = ['Maria', 'Julia', 'Pedro', 'Guilherme', 'Vanessa']

print([caixa_alta(amigo) for amigo in amigos])

# 3

print([numero * 3 for numero in range(1, 10)])

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])

