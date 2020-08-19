"""
Debuggando com PDB

PDB -> Python Debugger


# Exemplo com PyCharm


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return ('Valor Incorreto')
    except ZeroDivisionError:
        return 'Não é possivel dividir por zero'

print(dividir(4, 7))


"""

