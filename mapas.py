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

# Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamente de dicionarios

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Soma*, Valor Maximo*, Valor minimo*, Tamanho

# * se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))