"""
Entendo o *args

- O *args é um parametro como outro qualquer isso significa que vc pode chamar de qlqr coisa
desde que comece com '*'

Exemplo

*xis

Mas por conveção, utilizamos o *args para defini-lo

O parametro *args utilizado em func, coloca os valores extras informados como entrada em uma tupla.


def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))

# outro exemplo do args

def verifica_info(*args):
    if 'Python' in args and "Python2" in args:
        return 'Bem Vindo Python'
    return 'Não sei quem você é'

print(verifica_info())
print(verifica_info(1, True, 'Python', 'Python2'))
print(verifica_info(1, 'Python2', 3.145))

"""

def soma_todos_numeros(*args):
    return sum(args)

# Desempacotador


numeros = [1, 2, 3, 4, 5, 6, 7]

print(soma_todos_numeros(*numeros))

# O asterisco serve para que informemos ao Python que estamos usando um argumento de coleção de dados
# Desta forma ele sabe que precisa antes de tudo desempacotar os dados