"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

OBS.: com a herança a partir de uma class existente nos extendemos outra class
que passa a herdar os atributos e metodos da classe herdada.

Cliente
    - nome
    - sobrenome
    - cpf
    - renda

Funcionario
    - nome
    - sobrenome
    - cpf
    - matricula

"""
class Pessoa:

    def __index__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome}{self.__sobrenome}'


class Cliente(Pessoa):

    def __init__(self, renda):
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self, matricula):
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome}{self.__sobrenome}'


cliente = Cliente('Python', 'Python', '123.456.789-00', 5000)
funcionario = Funcionario('Python', 'Python', '987.654.321-11', '123')

print(cliente.nome_completo())
print(funcionario.nome_completo())