"""
StringIO

para ler ou escrever dados em arquivos do sistema operacional, o software precisa de permissão:

    - Permissão de leitura
    - Permissão de Escrita

StringIO - utilizado para ler e criar arquivos em memoria
"""

from io import StringIO

mensagem = 'String Normal'

# Podemos criar um arquivo em memoria já com uma string inserida, ou vazia para escrever depois

arquivo = StringIO(mensagem)

print(arquivo.read())