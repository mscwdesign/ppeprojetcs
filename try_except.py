"""
O bloco try/except

utilizamos o bloco try/except para tratar erros para tratar erros que podem ocorrer no nosso codigo
previnindo assim que o programa pare de funcionar e o usuario receba mensagens de erro.

a forma geral mais simples é

try:

    //execução problematica
except:
    //o que deve ser feito em caso de problema

# Exemplo 1 - Erro Generico

try:
    geek()
except:
    print('Deu algum problema')

OBS tratar erro de forma generica não é a melhor forma o ideal é sempre tratar de forma especifica.

# Exemplo 3 tratando erro especifico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')


# Exemplo 5 tratando erro especifico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro {err}')


# Exemplo 6

try:
    print('Geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu erro')

"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {"nome": "Python"}

print(pega_valor(dic, "game"))
