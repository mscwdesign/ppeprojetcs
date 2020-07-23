"""
Loop While

Forma geral

while expressao_boleana:
        //execução do loop

o bloco do while sera repetido enquanto a expressão boleana for verdadeira.

Expressão boleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:

num = 5

num < 5

Exemplo 1

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

#OBS: Em um loop while, é importante que cuidemos do criterio de parada.

"""

# Exemplo 2

resposta = ''

while resposta != 'sim':
    resposta = input('Ja acabou Jéssica?')