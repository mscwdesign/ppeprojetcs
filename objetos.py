"""
Objetos

São instancias das classes

Apos mapeamento do objeto do mundo real para sua representação computacional
devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/instancias de
uma classe como variaveis do tipo definido na classe.

"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Objetos

lamp = Lampada('branca', 110, 60)

cc = ContaCorrente(5000, 20000)

user = Usuario('Python', 'Org', 'python@python', '12345')