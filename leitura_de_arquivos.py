"""
Leitura de arquivos

Para ler um arquivo ou um conteudo em python utilizamos a função integrada open()
que significa abrir.

open() -> a forma mais simples de utilização nós passamos apenas um parametro de entrada,
que nesse caso é o caminho do arquivo a ser lido. Está função retorna um _io.TextIOWrapper e é com ele que
trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS por padrão a função open() abre o arquivo para leitura. Este arquivo deve existir ou então
será gerado o erro FileNotFoundError

"""

arquivo = open('texto.txt')

# print(arquivo)
# print(type(arquivo))

# Para ler o arquivo após a sua abertura usamos a função read()

ret = arquivo.read()

print(type(ret))
print(ret)

print(arquivo.read())

# OBS o Python utiliza um recurso para trabalhar com arquivos chamado cursos esse cursos
# funciona como o cursor quando estamos escrevendo

# A função read() le todo conteudo do arquivo.