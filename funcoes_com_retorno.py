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

"""

# Exemplo 1

def diz_oi():
    return 'Oi!'
    print('Estou sendo executado após o retorno')

print(diz_oi())