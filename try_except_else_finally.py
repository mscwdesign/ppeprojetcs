"""
Try, Except, Else, Finally

Dica de quando tratar o código

Toda entrada deve ser tratada


# Else exetuada somente se não ocorrer o erro

try:
    num = int(input('Informe um numero:'))
except ValueError:
    print('Valor Incorreto')
else:
    print(f'Você digitou {num}')


# Finally

try:
    num = int(input('Informe numero: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você não digitou um número {num}')
finally:
    print('Executando o finally')

# OBS o bloco finally é sempre executado

# o finally geralmente é utilizado para fechar ou desalocar recursos.



# Exemplo

def dividir(a, b):
    return a / b

num1 = int(input('Informe o primeiro numero: '))
try:
    num2 = int(input('Informe o segundo numero: '))
except ValueError:
    print('O valor precisa ser numerico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return ('Valor Incorreto')
    except ZeroDivisionError:
        return 'Não é possivel dividir por zero'


num1 = input('Informa o primeiro numero: ')
num2 = input(' Informa o segundo numero: ')

print(dividir(num1, num2))
"""


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return ('Valor Incorreto')
    except ZeroDivisionError:
        return 'Não é possivel dividir por zero'


num1 = input('Informa o primeiro numero: ')
num2 = input(' Informa o segundo numero: ')

print(dividir(num1, num2))
