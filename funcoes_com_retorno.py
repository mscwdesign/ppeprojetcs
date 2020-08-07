"""
Funções com retorno

numeros = [1, 2, 3]

ret = numeros.pop()
print(f'Retorno de Pop: {ret}')

ret = print(numeros)

print(f'Retorno de Print: {ret}')

OBS: em Python quando uma função não retorna nenhum valor o retorno é None

OBS: Funções Python que retornan valores devem retornar estes valores com a palavra reservada return

OBS não precisamos necessariamente criar uma variavel para receber o retorno de uma função
podemos passar a execução da função para outras funções.

# Refatorando função

def quadrado_de_7():
    return 7 * 7

# Criamos uma variavel para receber o retorno da função
ret = quadrado_de_7()

print(f'Retorno: {ret}')

print(f'Retorno: {quadrado_de_7()}')

# Refatorando a 1ª func

def diz_oi():
    return 'Oi '

alguem = 'Pedro!'

print(diz_oi() + alguem)

OBS Sobre a palavra reservada return

1 - Ela finaliza a função, ela sai da execução da função
2 - Podemos ter, em uma função diferentes returns;
3 - Podemos em uma função retornar qlqr tipo de dado e ate mesmo multiplos valores

# Exemplo 1

def diz_oi():
    return 'Oi!'
    print('Estou sendo executado após o retorno')

print(diz_oi())

# Exemplo 2

def nova_função():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_função())

# Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5

# num1, num2, num3, num4 = outra_funcao()

# print(outra_funcao())

print(outra_funcao())

# Vamos criar uma função para jogar cara ou coroa

from random import random

def joga_moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

# Refator de Func

def cantar_parabens(Aniversariante):
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {Aniversariante}!')

cantar_parabens('Marcos')


# Funções podem ter n parametros de entrada ou seja podemos receber como entrada
# quantos parametros forem necessarios, ele são separados por virgula.

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 +b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Python '))

#OBS se a gente informar um numero errado de paramtro da erro TypeError

# Nomear parametro

def nome_completo(nome, sobrenome):
    return (f'Seu nome completo é {nome} {sobrenome}')

print(nome_completo('Angelina', 'Jolie'))

# Dif parametro e Argumentos

# Parametros são Variaveis declaradas na definição de uma função
# Argumentos são dados passados durante a execução da função

# A ordem dos parametros importa

nome = 'Felicidade'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso seja utilizado nomes dos parametros nos argumentos p informa-los da para usar qlqr ordem

print(nome_completo(nome='Angelie', sobrenome='Jolie'))

"""

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))