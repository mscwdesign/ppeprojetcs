"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: o separador de casas decimais na programação é o ponto e não a virgula
"""

# Errado do ponto de vista do Floar, mas gera uma tupla
valor = 1,44

print(valor)

# Certo
valor = 1.44
print(valor)

# E possivel fazer dupla atribuição
valor1, valor = 1, 55

print(valor1)
print(valor)

# Podemos converter um Flot para um int
"""
OBS: ao converter valores float para inteiros nos perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com numeros complexos

variavel = 5j

