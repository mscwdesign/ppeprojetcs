"""
Decoradores - Decorators

São funções
Envolvem outras funções e aprimoram seus comportamentos
São exemplos de HOF
Tem sintax propria usando @ (Syntact Sugar)

# Teste 1

teste = seja_educado(saudacao())

teste()

# Exemplos sem a Syntact Sugar

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer lhe conhecer')
        funcao()
        print('Tenha um bom dia')
    return sendo


def saudacao():
    print('Seja bem vindo')


def raiva():
    print('Eu te Odeio')


raiva_educada = seja_educado(raiva)

raiva_educada()

# Exemplo som Syntax Sugar

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer te conhecer')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu Nome é Python')


apresentando()

@seja_educado_mesmo
def dormir():
    print('Quero Dormir')

dormir()

"""

