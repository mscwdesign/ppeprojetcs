"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas

Existem basicamente duas diferenças basicas

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutaveis: Isso significa que ao se criar uma tupla ele não muda.  Toda
operação em uma tupla gera uma nova tupla.


# Cuidado 1: As tuplas são representadas dpo (), mas veja:

#  print(type(()))

tupla1= (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5,
print(tupla2)

print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento

tupla3 = (1) # Isso não é uma tupla
print(tupla3)

print(type(tupla3))

tupla4 = (4,) #Isso é uma tupla!
print(tupla4)

print(type(tupla4))

tupla5 = 5,
print(tupla5)

print(type(tupla5))

# Conclusão: Podemos concluir que tuplas são definidas pela virgula e não pelo uso do parêntese.

(4) -> não é tupla
(4,) -> é tupla
4, -> é tupla

# Podemos gerar uma tupla dinamicamente com o range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamente de tupla

tupla = ('Geek', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# OBS: gera erro (valueError) se colocarmos um numero diferente de elementos para desempacotar.

# Metodos para adição, remoção de elementos nas tuplas não existem dado o fato das tuplas serem imutaveis.

# Soma*, Valor Máximo, Valor Minimo* e tamanho

# * se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6,)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de Tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # Tuplas são imutaveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

tupla1 = tupla1 + tupla2 # tuplas são imutaveis, mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)

# iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'd', 'e', 'a', 'b')

print(tupla.count('a'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

Parte da interação com meses segmento 2

print(meses)

# o acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# iterar com while

i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em ql indice um elemento está na tupla

print(meses.index('Junho'))

# Obs.: Caso o elemento não exista, gera erro. Value Error

print(meses.index('P'))

# Dicas na utilização de tuplas

# devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Slicing

# tupla[inicio:fim:passo]

print(meses[5:])

# Por que utilizar tuplas?

# - Tuplas são mais rápidas do que listas
# - Tuplas deixam seu código mais seguro

# * isto por que trabalhar com elementos imutaveis tras segurança para o código

# Copiando uma tupla para outra

tupla = (1, 2, 3,)
print(tupla)

nova = tupla # Na tupla não tem shallow copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)
"""




