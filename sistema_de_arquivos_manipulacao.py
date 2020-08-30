"""
Sistema de Arquivos - manipulação

# Descobrindo se um arquivo ou dir existe
print(os.path.exists('python.txt')) # True or False

# Diretorio

# Path relativo
print(os.path.exists('geek')) # True or false

# Path absoluto

print(os.path.exists('C:Windows'))
# Criando arquivos

open('arquivo-teste.txt', 'w').close()

#Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3

with open('arquivo-teste3.txt', 'a') as arquivo:
    pass

# Criando arquivos

os.mknod('arquivo-teste4.txt')

os.mknod('C:\\arquivo.txt')

# Se o arquivo já existe vai dar erro


os.mkdir('templates')

# Caso exista teremos erro de FileExistsError

# OBS caso não tivermos permissão para criar o dir teremos um erro de PermissionError

# Criando varios diretorios

os.makedirs('templates/geek/pyhton')

os.makedirs('templates2/novo2/outro2', exist_ok=True)
"""

import os

os.rename('templates', 'python2')