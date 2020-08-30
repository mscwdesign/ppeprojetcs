"""
o bloco with

o bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with.


"""

# o bloco with - a forma pythonica para manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.close())


print(arquivo.closed)