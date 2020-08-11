"""
Any e All

all() - retorna True se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel está vazio


# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # Todos verdadeiros ? False

print(all([1, 2, 3, 4]))  # Todos verdadeiros ? True

print(all([]))  # Todos verdadeiros ? True

print(all((1, 2, 3, 4)))  # Todos verdadeiros ? True

print(all({1, 2, 3, 4}))  # Todos verdadeiros ? True

nomes = ['Calors', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))

# OBS um iteravel fazio convertido em Boolean é False mas o all() entende como True
print(all([letra for letra in '' if letra in 'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))


any() -> retorna true se qlqr elemento do iteravel for vddeiro, se estiver vazio é false


"""

print(any([0, 1, 2, 3, 4])) # True

print(any([0, False, {}, (), []])) # False

nomes = ['Calors', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(any([0] == 'C' for nome in nomes))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))
