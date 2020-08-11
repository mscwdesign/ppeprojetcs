"""
Lambdas

Conhecidas por Expressões Lambdas, ou Lambdas = Funções sem nome "Funções Anonimas"

def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(100))


# Exemplo com lambda

lambda x: 3 * x + 1

calc = lambda x: 3 * x + 1

print(calc(1))
print(calc(100))

# Podemos ter expressões lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' Angelina', ' JOLIE'))

# Funções Python podem ter nenhuma, ou varias entradas em lambdas também

amar = lambda: 'Python'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(uma(6))
print(duas(5, 6))
print(tres(3, 6, 9))

# Exemplo

autores = ['Isac Asimov', 'Ray', 'Robert', 'Arthur', 'Frank', ' Orson', 'Douglas', 'Wells', 'Leight Bracket']
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

"""

# Função quadratica

# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    """ Retorna a função f(x) = a * x ** 2 + b * x + c """
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))
