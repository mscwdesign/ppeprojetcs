"""
Levantando proprios erros com raise

raise -> Lança exceções

OBS, o raise não é uma função é uma palavra reservada assim como def ou qlqr outra em Python

A forma geral, de utilização é

raise TipoDoErro('Mensagem de Erro')


# Exemplo

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma String')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Python', 'Verde')

#   Exemplo refatorado
OBS o raise finaliza a função nada abaixo dele é executado

# Exemplo

def colore(texto, cor):
    cores = ['Verde', 'Amarelo', 'Azul', 'Branco']
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma String')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Python', 'Laranja')

"""

# Exemplo

def colore(texto, cor):
    cores = ['Verde', 'Amarelo', 'Azul', 'Branco']
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma String')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Python', 'Laranja')

