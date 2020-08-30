"""
Para fazer uso de manipulação de arquivos precisamos importar e fazer uso do modo OS

os -> Operating System


# getcwd() -> pega o current work directory - diretório de trabalho corrento
# Retorna o path(caminho) absoluto
print(os.getcwd())

# Para mudar o diretorio, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())

# checando diretorio relativo ou absoluto

print(os.path.isabs('C:\\'))

# podemos identificar o OS com o módulo 'os'

print(os.name) # posix linux e mac nt windows


# Fazer import
import os


# podemos ter mais detalhes do OS

print(os.uname()) # no windows não funfa


import sys

print(sys.platform)
"""

import os

