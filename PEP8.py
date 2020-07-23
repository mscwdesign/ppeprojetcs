"""
PEP8 - Python Enhancement Proposal

São propstas de melhorias para a linguagem Python

Zen of python

A ideia do PEP8 é que possamos escrever códigos Python de forma pythonica.

[1] -  Utilize Camel Case para nome de classes;


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] -  Utilize nomes em minúsculo, separados por undeline para funções ou variáveis;


def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identação!

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- Metodos dentro de uma classe devem ser separados com uma unica linha em branco;

[5] - Imports

# Import Errado

import sys, os

# Import Certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer;

from types import (
    StringType
    ListType
    SetType
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentarios ou docsstrings e antes de constantes ou variaves globais

- Immports devem ser sempre feitos em linhas separadas;

[6] - Espaços em expressões e instruções

# Não faça:

funcao9( algo[ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não faça:

algo (1)

# Faça:

algo(1)

# Não faça:

dict ['chave'] = list [indice]

# Faça;

dict['chave']=lista[indice]

# Não faça:

x           = 1
y           = 3
variavel_longa = 5

#Faça

x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha:
"""
