"""
Geradores

 - Geradores(Generators) são iteradores

OBS o contrario não é verdadeiro, ou seja nem todo iterator é um generator.

- Generators podem ser criados com funções geradoras
- Funções geradoras utilizam a palavra reservada yield
- Generators podem ser criados com Expressões Geradoras

Diferenças entre funções e Generators Functions

_______________________________________________________________
|Funções                           |Generators Functions
---------------------------------------------------------------
Utiliza Return                      utiliza yield
retorna uma vez                     pode utilizar yield múltiplas vezes
retorna um valor                    retorna um generator


for num in gen:
    print(num)
"""

# Exemplo de Generator Function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


# uma generator function não é um generator, ela gera um generator

gen = conta_ate(10)

print(next(gen))

for num in gen:
    print(num)

