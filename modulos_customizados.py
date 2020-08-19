"""
Módulos Customizados

Como módulos python nada mais são do que arquivos python então todos os programas ou todos os arquivos que criamos neste
curso são módulos python prontos para serem utilizandos

# Importando uma função especifica do nosso modulo
from funcoes_com_retorno import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 6, 7]))


# Import todo modulo

import funcoes_com_retorno as fcp

print(fcp.lista)

print(fcp.tupla)

"""

from map import cidade, c_para_f

print(list(map(c_para_f, cidade)))