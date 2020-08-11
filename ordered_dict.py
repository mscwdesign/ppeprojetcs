"""

Modulo Collections: Ordered Dict

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

OrderedDict -> É um dicionario, que nos garante a ordem de inserção dos elementos.

# Fazer import

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

"""
from collections import OrderedDict

# Entender a dif entre os dicts

# Dict comun

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1==dict2) #  é True pq a ordem não importa para o dict

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1==odict2)   # é Falso pq a ordem importa no ODICT