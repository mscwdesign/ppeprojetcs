"""
List Comprehension

Podemos add estruturas condicionais logicas

"""

# Exemplo

numeros = [1, 2, 3, 4, 5]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refator
# Qlqr num par modulo de 2 é 0 é 0 em python é false, not False = True

pares = [numero for numero in numeros if not numero % 2]
pares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)