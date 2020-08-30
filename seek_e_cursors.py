"""
Seek e Cursors

seek() é utilizado para movimentar o cursor


arquivo = open('texto.txt')

print(arquivo.read())


# seek()  serve para movimentação do cursor pelo arquivo, ela recebe um parametro que indica onde por o cursor
# Movimentar o cursor pelo arquivo com seek()

arquivo.seek(0)

print((arquivo.read()))

arquivo = open('texto.txt')

print(arquivo.read())

#readline() le por linhas

print(arquivo.readline())


#readlines()

print(arquivo.readlines())

linhas = arquivo.readlines()

print(len(linhas))

Ao abrir com o open() é criado uma conexão entre o arquivo e o nosso programa, isso se chama streaming
ao finalizar o trabalho devemos fechar essa conexão usando a função close()

1 - Abre o arquivo
2 - Trabalho o arquivo
3 - Fechar o arquivo

# Abrindo o arquivo
arquivo = open('texto.txt')

# Trabalhando o arquivo
print(arquivo.read())

print(arquivo.closed)

# Fecha o arquivo
arquivo.close()

print(arquivo.closed)

"""

arquivo = open('texto.txt')

# Com a função read da para limitar a leitura

print(arquivo.readlines(50))