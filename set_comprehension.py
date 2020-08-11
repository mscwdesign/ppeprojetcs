"""
Set Comprehension

"""

# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# Exemplo 2

numeros = {x: x * 2 for x in range(10)}
print(numeros)

letras = {letra for letra in ' Python'}

print(letras)
