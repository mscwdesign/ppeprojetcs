"""
Funções com Parametro Padrão (Default Parameters)

- Func onde a passagem de parametro seja opcional

# Exemplo

print('Python')
print()

# Exemplo Parametro obrigatorio

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado())

def exponecial(numero, potencia=2):
    return numero ** potencia

print(exponecial(10, 2))

print(exponecial(3))

# Se o usuario passar só 1 argumento ele é dado ao parametro numero e calcula sobre ele
# se o usuario passar 2 argumento o primeiro sera atribuido ao numero e o segundo ao parametro potencia
# Será calculada a esta potencia

# OBS: Em funções Python os parametros com valores Default DEVEM sempre estar ao final da declaração.

# erro

def teste(num=2, potencia):
    return num ** potencia

print(teste(6))


# Outros exemplos

def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))
print(soma(4)) # Erro
print(soma()) # Erro

# Exemplo complexo

def mostra_informacao(nome='Python', instrutor=False):
    if nome == 'Python' and instrutor:
        return 'Bem Vindo Python'
    elif nome == "Python":
        return 'Você não é Python'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))


# Por que utilizar parametros com valor default

# Nos permite maior flexiblidade na função
# Evita erro com parametros incorretos
# Exemplos mais legiveis de código

# Quais tipos de dados podemos utiliza nos valores default = Todos os tipos de dados

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 5))
print(mat(2, 2, subtracao))

# escopo - evita problemas

# Variaveis globais
# Variaveis Locais

instrutor = 'Python'    # Global

def diz_oi():
    instrutor = 'Python2'
    return f'Oi {instrutor}'

print(diz_oi())

# A Variavel local se tiver o mesmo nome da global, a local tem preferencia.

def diz_oi():
    prof = 'Python'
    return f'Olá {prof}'

print(diz_oi())
print(prof)

# Atenção com Variaveis globais ( Se puder evite )

total = 0

def incrementa():
    total = total + 1
    return total


print(incrementa())

# Atenção com Variaveis globais ( Se puder evite )

total = 0

def incrementa():
    global total
    total = total + 1
    return total


print(incrementa())

# Podemos ter função dentro de função / Existem formas especiais de escopo de variavel

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())

"""

