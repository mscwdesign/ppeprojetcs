"""
Recebendo dados do usuario

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas Simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'angelina'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""
# Aspas duplas triplas -> """Angelina Jolie"""

# Exemplo antigo versão 2.x

# print('Qual seu nome?')
# nome = input()  # Input -> Entrada

# print('Seja bem vindo(a) %s' % nome)

# print('Qual sua idade?')
# idade = input()

# Processamento

# Saida

# print('O %s tem %s anos' % (nome, idade))


# Exemplo de print da versão 3.x

# print("Qual seu nome?")
# nome = input()

# print('Seja bem-vindo(a) {0}'.format(nome))

# print("Qual sua idade")
# idade = input()

# print('A {0} tem {1} anos'.format(nome, idade))


# Exemplo de print mais atual 3.7x

# print('Qual seu nome?')
# nome = input()

# print(f'Seja bem-vindo(a) {nome}')

# print('Qual sua idade?')
# idade = input()

# print(f'{nome} tem {idade} anos')

# print(f'A {nome} nasceu em {2019 - int(idade)}')

# Exemplo Simplificado

nome = input('Qual seu nome?')
idade = input('Qual sua idade?')
print(f'A {nome} nasceu em {2019 - int(idade)}')

