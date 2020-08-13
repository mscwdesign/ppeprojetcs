"""
Zip

zip() -> Ele cria um iteral (ZIP OBJECT) que agrega elemento de cada um dos iteraveis passados em pares

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(list(zip1))

# OBS: o zip() utiliza como parametro o menor tamanho em iteravel.
# Isso siginifica que se tiver trabalhando com iteraveis de tamanhos diferentes ele para quando
# o menor iteravel for identificad
lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# lista de tuplas

dados = [(0, 1), (2, 3), (4, 5)]
print(list(zip(*dados)))


"""

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

# podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))


