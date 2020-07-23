"""
Escopo de variáveis

Dois casos de escop:

1 - Variaveis globais;
    - Variaveis globais sao reconhecidas, ou seja, seu escopo compreende todo o programa

2 - Variaveis locais;
    - Variaveis locais sao reconhecidas apenas no bloco onde foram declaradas, ou seja
    seu escopo está limitado ao bloco onde foi declarada

Para declarar variaveis em Python seguimos:

nome_da_variaval = valor_da_variavel

Python é uma linguagem de tipagem dinamica, isso significa que ao declararmos uma variavel,
nos não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuido valor a mesma.

Exemplo em C:
int numero = 42:

Exemplo em java:
int numero = 42:

"""

numero = 42     # Variavel global
print(numero)
print(type(numero))

numero = 'Geek'     # Variavel local
print(numero)
print(type(numero))

nao_existo = 'Oi'

print(nao_existo)
print(type(nao_existo))

numero = 10
novo = 0

if numero > 10:
    novo = numero + 10  # A Variavel novo está declarada localmente dentro do bloco. Portanto é local
    print(novo)

print(novo)