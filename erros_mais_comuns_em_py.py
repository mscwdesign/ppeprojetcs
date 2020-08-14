"""
Erros mais comuns em Python

1 - SyntaxError -> Erro de Syntax ou erro de escrita

a) def funcao:
    print('Python')

# Named error

2 - Quando a variavel ou a função não está definida

a = 18
if a < 10:
    msg = 'E maior que 10'

print(msg)

3 - TypeError -> Função/Operação/Ação é aplicada a um tipo errado

a)
print(len(5))

b)
print('Python' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em lista ou outros tipos de dados
utilizando indices invalidos

a)
lista = ['Python']
print(lista[2])


5 - > ValueError, funções built-in recebem argumentos com tipo correto mas valor inapropriado

a)
print(int('Geek'))

6 -> KeyError Ocorre quando tentamos acessar o dicionario com chaves inexistentes

a)
dic = {}
print(dic['geek'])

7 -> AttributeError Quando a variavel não tem um atributo/função

a)
tupla = (11, 2, 21, 34, 1)
print(tupla.sort())

8 -> IdentationError -> Ocorre quando não respeitamos a identação do Python ( 4 espaços )

a)
def nova():
print('Geek')

b)
for i in range(10):
i + 1

"""


