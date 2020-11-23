"""
Metodos

metodos(funções) representam os comportamentos do objeto. Ou seja as ações que este objeto pode
realizar no seu sistema

Em python dividimos os metodos em 2 grupos: Metodos de instancia e Metodo de classe

o metodo init __init__ é um método especial chamado de construtor e sua função é construir
o objeto a partir da classe

p1 = Produto('PS4', 'Video Game', 2300)

print(p1.desconto(50))


user1 = Usuario('Python', 'Programa', 'python@python.com.br', '123456')

print(user1.nome_completo())

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(42)

print('Usuario criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')


print(f'Senha User Criptografada: {user._Usuario__senha}')


# Metodo de Classe

user = Usuario('adm', 'adm', 'adm@adm.com.br', '1234')

Usuario.conta_usuario()
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        ContaCorrente.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto."""
        return (self.__valor * (100 - porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuarios no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def __correr__(self, metros):
        print(f'{self.__nome} está correndo {metros} metros')

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


