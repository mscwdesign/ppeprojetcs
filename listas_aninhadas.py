"""
Listas aninhadas

Algumas linguagens de prog possuem uma estrutura de dados "arrays"
Unidimensionais (Arrays/Vetores)
Multidimensionais (Matrizes)

Python tem as listas

print(listas)
print(type(listas))

# Acessando os dados

print(listas[0][1])
print(listas[2][1])

# Iterar

for lista in listas:
    for numero in lista:
        print(numero)

# Exemplo

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



# List Comprehension

[[print(valor) for valor in lista] for lista in listas]

"""

# Outro exemplo

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Exemplo valores

print([['*' for i in range(1, 4)] for j in range(1, 4)])