"""
Dicionarios

Obs.: em algumas linguagens de programação, os dicionarios Python são conhecidos por mapas.

Dicionarios são coleções do tipo chave/valor.

Dicionarios são representados por {}.

print(type({}))

OBS: Sobre dicionarios
    - Chave e valor são separados por dois pontos 'chave:valor'
    - Tanto chave quanto valor podem ser de qualquer tipo de dados
    - Podemos misturar tipos de dados;

# Criação de Dicionarios

# Forma 1 - mais comum

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 - menos comum

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via Chave da mesma forma que lista/tupla

print(paises['br'])
# print(paises['ru'])

# Caso tente fazer o acesso com chaves inexistentes gera o erro KeyError

# Forma 2 - acessando via get - Recomendado

print(paises.get('br'))
print(paises.get('ru'))

# Metodo para encontrar o valor usando a função get

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não sera gerado
KeyError

pais = paises.get('ru')


if pais:
    print(f'Encontrei o pais {pais}')
else:
    print('Não encontrei o pais')

# OBs podemos definir um valor padrão
caso não encontremos o objeto com a chave informada

pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o pais {pais}')

# Podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qlqr tipo de dado (int, float, string, boolean), inclusive lista/tupla, dicionario
# como chaves de dicionario.


# Tuplas por exemplo são bastante interessante de serem utilidas como chave de dicionarios, pois as mesmas
# são imutaveis.

localidades = {
    (35.6895, 39.6917): 'Escritorio em Tokio',
    (40.7128, 74.0060): 'Escritorio em NY',
    (37.7749, 122.4194): 'Escritorio em Sao Paulo',

}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# forma 1 - Mais comum

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado) # receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionario

# Forma 1

receita ['mai'] = 550

print(receita)

#Forma 2

receita.update({'mai': 600})

print(receita)

# Conclusão 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma.
# Conclusão 2: Em dicionarios não podemos ter chaves repetidas.


# Remover dados de um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 - Mais comum

ret = receita.pop('mar')
print(ret)

print(receita)

# OBS aqui sempre precisamos informar a chave, caso não não encontre gera KeyError
# OBS ao removermos um objeto o valor deste objeto é sempre retornado.

# Forma 2
del receita['fev']

print(receita)

del receita['fev']

# OBS se a chave não existir sera gerado um KeyError
# Neste caso o valor removido não é retornado.

"""

# Imagine que vc tem um comercio eletronico onde temos um carrinho de compras na qual adicionamos
# produtos

"""
Carrinho de Compras
    Produto 1
        - nome;
        - quantidade;
        - preço;
    Produto 2
        - nome;
        - quantidade;
        - preço;


# 1 -  Poderiamos usar uma lista para isso? Sim

carrinho = []

produto1 = ['PS4', 1, 230.00]
produto2 = ['PS3', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto.

# 2 - Poderiamos usar uma tupla para isto? Sim

produto1 = ('PS4', 1, 2.300)
produto2 = ('PS3', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teriamos que saber qual é o indice de cada informação do produto.

# 3 - Poderiamos usar o dicionario para isso? Sim

carrinho = []

produto1 = {'nome': 'PS4', 'quantidade': 1, 'preço': 2.300}
produto2 = {'nome': 'PS3', 'quantidade': 1, 'preço': 300.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Deste forma facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação

# Limpar o dicionario zerar dados

d.clear()
print(d)

# Metodos de dicionarios

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Copiando um dicionario para outro

# Forma 1 # Deep Copy

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

"""

# Forma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# o metodo fromkeys recebe dois parametros  um iteravel e um valor.
# Ele vai gerar para cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)


veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)