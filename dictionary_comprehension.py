"""
Dictionary Comprehension

Se quiser criar uma lista :

lista = [1, 2, 3]
tupla = (1, 2, 3,)
conjunto = {1, 2, 3}
dicionario = {'a': 1, 'b': 2, 'c': 3}

{chave:valor for valor in iteravel}

# Exemplo

numeros = {'a': 1, 'b': 2, 'c': 3}

quadrado = {chave : valor ** 2 for chave, valor in numeros.items()}

print(quadrado)


# Exemplo

numero = [1, 2, 3]

quadrados = {valor: valor ** 2 for valor in numero}

print(quadrados)

# Exemplo

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)


"""

# Exemplo

numeros = [1, 2, 3, 4, 5]

res = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)