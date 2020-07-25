"""
Conjuntos

- Conjuntos em qualquer linguagem de programação estamos fazendo referencia a teoria dos conjuntos da matematica

- Aqui no python os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valore duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos não nos importamos com a ordenação deles.
Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferenças entre Conjuntos (Sets) e Mapas (dicionarios) em Python:
    - Um dicionario tem Chave/Valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto

#Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3, 4,})

print(s)
print(type(s))

# OBS: ao criar um conjunto caso seja adicionado um valor já existente o mesmo sera ignorado sem gerar erros e não fara
# parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 3, 4, 5, 6}

print(s)
print(type(s))

# Podemos verificar se o determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem.

# Listas aceitam valores duplicados então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista:{lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados então temos 10 elementos
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios não aceitam Chaves duplicados então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets

# Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu e os visitantes informaram
# manualmente a cidade de onde vieram.

# nos adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja unicas temos.

# O que você faria?

# podemos utilizar o set

print(len(set(cidades)))

# Adicionando elementos em um conjunto.

s = {1, 2, 3,}

s.add(4)
s.add(4) # Duplicidade não gera erro, somente é ignorado e não é adicionado
print(s)

# Removendo elementos de um conjunto.

#Forma 1
s = {1, 2, 3,}
print(s)

s.remove(3) # Não é indice, informamos o valor a ser removido
print(s)

# OBS caso o valor não seja encontrado será gerado o erro KeyError
# Nenhum valor é retornado

# Forma 2

s.discard(2)
print(s)

#OBS se o valor não for encontrado nenhum erro é gerado.

# Copiando um conjunto para outro
# Forma 1 - Deep copy

novo = s.copy()
print(novo)

novo.add(4)
print(novo)
print(s)

# Forma 2 - Shallow Copy

novo = s
novo.add(4)
print(novo)
print(s)


s = {1, 2, 3}
print(s)

# Podemos remover todos os itens do conjunto

s.clear()
print(s)

"""

# Metodos matemáticos de conjuntos

# Imagine que temos dois conjuntos um contendo estudantes do curso python e um contendo estudantes do curso de java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam python tbm estudam java.

# Precisamos gerar um conjunto com nomes de estudantes unicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)