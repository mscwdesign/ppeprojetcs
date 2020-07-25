"""
Módulo Collections - Counter

Collections -> High-performance Container Datetypes

Counter -> Recebe um iteravel como parametro e cria um objeto do tipo Collections Counter que é parecido com
um dicionario contendo como chave o elemento da lista passada como parametro e como valor a quantidade
de ocorrencias desse elemento.


# Realizando o import

from collections import Counter

# Podemos utilizar qualquer iteravel aqui usamos lista
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

# Counter({1: 6, 2: 6, 3: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})
# Para cada elemento da lista o Counter criou uma chave e colocou como valor a quantidade de ocorrencias.


print(Counter('Geek University'))

# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
"""

from collections import Counter

texto = """ Mussum Ipsum, cacilds vidis litro abertis. Nullam volutpat risus nec leo commodo, ut interdum diam laoreet.
Sed non consequat odio. Manduma pindureta quium dia nois paga. Tá deprimidis, eu conheço uma cachacis que pode alegrar
sua vidis. Atirei o pau no gatis, per gatis num morreus.  """

palavras = texto.split()
# print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(5))