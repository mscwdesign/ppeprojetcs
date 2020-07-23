"""
Loop for

loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < limitador; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop



Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis

Exemplos de iteraveis
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range (1, 10)
"""
"""
# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1, 10):
    print(numero)

OBS: Quando não precisamos de um valor, podemos descartá-lo utlizando um underline(_)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em lista5

for valor in enumerate(nome):
    print(valor)
    
qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Teste Python'
for letra in nome:
    print(letra, end='')

Tabela  de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode#block-1-emoticons
"""

# Original: U+1F605
# Modificado: U0001F60D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)
