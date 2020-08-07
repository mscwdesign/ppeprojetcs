"""
**kwargs

Este é um parametro que diferente do args coloca os valores extras em tupla mas o kwargs exige
parametros nomeados e o extras ficam em um dicionario

# Exemplo

def cores_favoritas(**kwars):
    for pessoa, cor in kwars.items():
        print(f'A cor favorita da {pessoa.title()} é {cor}')

cores_favoritas(marcos='Verde', julia='Amarelo', fernando='Azul')

# OBS os parametros *args e **kwargs não são obrigatorios

# Exemplo mais dificil

def cumprimento_especial(**kwargs):
    if 'Python' in kwargs and kwargs['Python'] == 'Geek':
        return 'Voce foi comprimentado'
    elif 'Python' in kwargs:
        return f"{kwargs['Python']} Geek"
    return 'Não te conheço'

print(cumprimento_especial())
print(cumprimento_especial(Python='Geek'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(Python='Olá'))
print(cumprimento_especial())

# Nas func podemos ter - segue ordem

- Parametros obrigatorios
- *args
- Parametros Defalut
- **kwars


def minha_funcao(num, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {num} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicidade', 4, 5, 6, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

"""

