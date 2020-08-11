"""
Map

Com map fazemos mapeamento de valores para função.

import math


def area(r):
    #Calcula a area de um circulo com raio 'r'#
    return math.pi * (r ** 2)

print(area(2))
print(area(5.2))

raios = [1, 2, 3, 4, 5, 6, 10, 25, 5.5, 10.10]

areas = []
for r in raios:
    areas.append((area(r)))

print(area(r))

# Forma 2

areas = map(area, raios)
print(list(areas))

# Forma 3 Usando Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS após utilizar a func map depois da primeira utilização do resultado ele zera.

# Map

# Dados iteraveis

# dados: a1, a2, an....

# Temos uma função

# Função: f(x)

# utilizamos a função map(f, dados) onde ira mapear cada elemnteo dos dados e aplica a função.

# O map object: f(a1), f(...), f(an)

"""

# Exemplo

cidade = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27)]

# f = 9/5 * c + 32

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidade)))

