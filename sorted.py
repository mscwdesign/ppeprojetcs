"""
Sorted

Não confunda com sort() q já estudamos em listas. O sort()

Podemos utilizar o sorted() com qlqr iteravel

Como o proprio nome diz o sorted() serve para ordenar

OBS o sorted() sempre retorna uma lista, com os elementos do iteravel ordenados

# Exemplo

numeros = [6, 1, 8, 2]

print(sorted(numeros)) # Ordenar do maior para o menor

print(numeros)

# Adicionando parametros ao sorted()

numeros = [6, 1, 8, 2]

print(sorted(numeros, reverse=True))


usuarios = [
    {"username": "samuel", "tweets": ["Adoro Bolo", "Adoro Pizzas"]},
    {"username": "carla", "tweets": ["Amo gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Amo cães", "Vamos sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)
print(sorted(usuarios, key=lambda usuario: usuario["username"]))
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))


"""

# Exemplo

musicas = [
    {"titulo": "Rise", "tocou": 3},
    {"titulo": "Awake", "tocou": 10},
    {"titulo": "Skillet", "tocou": 3},
    {"titulo": "Skill", "tocou": 100},
    {"titulo": "Tks", "tocou": 1000},
    {"titulo": "Green Day", "tocou": 116254},
    {"titulo": "NF", "tocou": 3 * 123467212837618263},

]

print(sorted(musicas, key=lambda musica:musica['tocou']))
print(sorted(musicas, key=lambda musica:musica['tocou'], reverse=True))