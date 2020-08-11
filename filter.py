"""
Filter

filter() - serve para filtrar dados de uma determinada coleção

#Biblioteca para trabalhar com dados estatisticos
import statistics

# Dados do sensor

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)

# Assim como a função map a filter recebe dois parametros, sendo uma função e um iteravel.

res = filter(lambda x: x > media, dados)
print(list(res))

# OBS assim como na função mpa(), após serem utilizados os dados de filter eles são excluidos da memoria.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(None, paises)
print(list(res))


paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))


# a diferença entre map e filter é

# map() -> Recebe dois parametros, uma função e um iteravel e retorna um objeto mapeando a função de cada elemento
do iteravel

# filter() -> Recebe dois parametros uma função e um iteravel e retorna um objeto filtrando apenas os elementos
de acordo com a função


# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Adoro Bolo", "Adoro Pizzas"]},
    {"username": "carla", "tweets": ["Amo gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Amo cães", "Vamos sair hoje"]},
    {"username": "gal", "tweets": []}
]

# Filtrar os usuarios que estão inativos no Twitter

inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)


"""

# Combinando filter e map

nomes = ['Vanessa', 'Ana', 'Maria']

# Objetivo Criar lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)