"""
Min e Max

lista = [1, 2, 3, 4, 5]
print(max(lista))

tupla = (1, 2, 3, 4, 5)
print(max(tupla))

conjunto = {1, 2, 3, 4, 5}
print(max(conjunto))

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(max(dicionario.values()))


val1 = int(input('Informe o Valor'))
val2 = int(input('Informe o Valor 2'))

print(max(val1, val2))

# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tin', 'Wash']

print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

"""

musicas = [
    {"titulo": "Rise", "tocou": 3},
    {"titulo": "Awake", "tocou": 10},
    {"titulo": "Skillet", "tocou": 3},
    {"titulo": "Skill", "tocou": 100},
    {"titulo": "Tks", "tocou": 1000},
    {"titulo": "Green Day", "tocou": 116254},
    {"titulo": "NF", "tocou": 123467212837618263},

]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))


print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 99999

for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])

