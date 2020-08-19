"""
Dunder Name e Dunder Main

Dunder Name -> __name__

Dunder Main -> __main__

Em Python são utilizados dunder para criar funções, atribtos e propriedades utilizando
Double Under para não gerar conflito na programação.

Se executarmos um modulo Python diretamente na linha de comando, internamente o python atribuira
a variavel Dunder Name o valor Main indicando que esse modulo é o de execução principal.

"""

from funcoes_com_retorno import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8]))