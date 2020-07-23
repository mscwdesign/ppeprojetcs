"""
Listas

Listas em Python funcionam como como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dados.

- Dinamico: Não possui tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando
elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qlqr tipo de dado;

As listas em Python são representadas por colchetes []
"""
"""

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['g', 'e', 'e', 'k']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek')

# Podemos facilmente checar se determinado valor está contido na lista;

num = 0

if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')

# Podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrencias de um valor em uma lista

print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas


Para adicionar elementos em listas, utilizamos a função append

OBS: Com append, nos só conseguimos adicionar 1 elemento por vez.

print(lista1)
lista1.append(42)
print(lista1)
lista1.sort()
print(lista1)

if 42 in lista1:
    print('É verdadeiro')
else:
    print('Não é verdade!')

# Erro mais de um argumento.             lista1.append(12, 34, 56)

lista1.append([8, 3, 1])     # Coloca a lista como elemento unico ( sublista )
print(lista1)

if [8, 3, 1] in lista1:
    print('Econtrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional a lista.
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do indice
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente juntar duas listas

# lista.extend(lista2)

lista6 = lista1 + lista2
print(lista6)

# Reverter a Lista
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

print(lista1[::-1])
print(lista2)

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos tem dentro da lista.
print(len(lista2))

# Podemos remover facilmente o ultimo elemento de uma lista.
# O pop não somente remove o ultimo elemento mas também o retorna.

print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemnto pelo indice
# Os elementos á direita deste indice serão deslocados para a esquerda.

lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos ( zerar a lista )

print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente converter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, o Split separa os elementos da da lista pelo espaço entre elas.

# Exemplo 2

curso = 'Programação, em, Python'
print(curso)
curso.split(',')
print(curso)

# Convertendo uma lista em uma String / Pega a lista 6 coloca um espaço entre cada elementro e transforma em uma string

lista6 = ['Programação', 'Python']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string

curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, coloca $ entre cada elemento e transforma em uma string

curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345345]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 utilizando for

soma = 0

for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando While

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # Imprime 'Verde'
print(cores[1]) # Imprime 'Amarelo'
print(cores[2]) # Imprime 'Azul'
print(cores[3]) # Imprime 'Branco'

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o indice negativo, pensa na lista como um círculo, onde
# O final de um elemento está ligado ao início da lista. 

print(cores[-1]) # Imprime 'Branco'
print(cores[-2]) # Imprime 'Azul'
print(cores[-3]) # Imprime 'Amarelo'
print(cores[-4]) # Imprime 'Verde'

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

cores = ['verde', 'amarelo', 'azul', 'branco']

# Gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repeditos
lista = []
lista.append(42)
lista.append(42)
lista.append(4)
lista.append(29)

print(lista)

# Outros metodos não tão impostantes mas também úteis

# Encontrar o indice de um elemento na lista

# Em qual indice está o valor 6?
numeros = [5, 6, 7, 8, 5, 9, 10]
print(numeros.index(6))

# Em qual indice está o valor 9?
print(numeros.index(9))

# Obs: caso não tenha este elemento na lista será apresentado erro.

print(numeros.index(5)) # Retorna o indice do primeiro elemento encontrado

# Podemos fazer busca dentro de um range, ou seja qual indice começar a buscar
print(numeros.index(5, 1)) # Buscando a partir do indice 1
print(numeros.index(5, 2)) # Buscando a partir do indice 2
print(numeros.index(5, 3)) # Buscando a partir do indice 3
print(numeros.index(5, 4)) # Buscando a partir do indice 4

# OBS: caso não tenha este elemento na lista será apresentado erro.

# Podemos fazer busca dentro de um range inicio/fim

print(numeros.index(8, 3, 8)) # Buscar o indice do valor 8, entre os indices 6 e 8.

# Revisão Slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de lista com o parametro inicio

lista = [1, 2, 3, 4]
print(lista[1:]) # Iniciando no indice 1 e pegando todos os elementos restantes.

# Trabalhando com slice de lista com o parametro fim

print(lista[:2]) # Começa em 0 pega até o indice 2 -1

print(lista[:4]) # Começa em 0 pega até o indice 4 -1

print(lista[1:3]) # Começa em 1 pega até o indice 3 -1

# Trabalhando com slice de lista com o parametro 'passo'

print(lista[1::2]) # Começa em 1, vai até o final, de 2 em 2.

print(lista[::2]) # Começa em 0, e vai até o final, de 2 em 2.

# Invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes = ['Geek', 'University']

nomes.reverse()
print(nomes)

# Soma*, valor maximo*, valor minimo*, tamanho*

# * Se os valores forem todos inteiros ou reais

lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 111)

print(sum(lista)) # Soma
print(max(lista)) # maximo valor
print(min(lista)) # minimo valor
print(len(lista)) # tamanho da lista

# Transformar uma lista em tupla
lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 111)
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))


# Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3, = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um numero diferente de elementos na lista ou variaveis 
# para receber os dados, teremos ValueError.

# Copiando uma lista para outra (Shallow Copy e Deep Copy)
# Forma1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy() # cópia

print(nova)

nova.append(4)
print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas
# elas ficaram totalmente independentes, ou seja, modificando uma lista não afeta a outra.
# Isso em Python é chamado de Deep Copy (Copia Profunda)

# Forma 2 - Shallow copy

lista = [1, 2, 3]
print(lista)

nova = lista  # cópia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, 
# mas após realizar modificação em uma das listas , essa modificação se reflete em ambas as listas
# Isso em Python é chamado de Shallow Copy.
"""

