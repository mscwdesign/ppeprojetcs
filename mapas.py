"""
Mapas são conhecidos em python como dicionarios

Dicionarios em Python são representados por chaves.

# Como interar sobre dicionarios

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'EM {chave} recebi R$ : {receita[chave]}')

print(receita)

# Acessando as chaves

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}


# Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)