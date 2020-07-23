"""
Tipo booleano

Algebra booleana, criado por George Boole

2 constante, Verdadeiro ou Falso

True -> Verdadeiro
False -> False

OBS: Sempre com a inicial Maiuscula

Errado:

true, false

Certo:

True, False

"""

ativo = True

print(ativo)

"""
Operações básicas:
"""

# Negação (not):

"""
Fazendo a negação se o valor booleano for verdadeiro o resultado será falso
se for falso o resultado será verdadeiro, ou seja sempre o contrario. 
"""

print(not ativo)

logado = False

# Ou (or)
"""
É uma operação binaria ou seja depende de dois valores. Ou um ou outro deve ser
verdadeiro. 

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""

print(ativo or logado)

# E (and):

"""
Também é uma operação binaria, ou seja, depende de dois valores. Ambos devem ser 
verdadeiros

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""