"""
Modo de abertura


r -> abre para a leitura
w -> abre para a escrita - acaba sobre escrevendo
x -> abre para a escrita somente se o arquivo não existir
a -> abre para escrita adicionando o conteudo ao final do arquivo
+ -> abre para o modo de att leitura e escrita

# OBS 'a' abrindo no modo 'a' se o arquivo não existir ele cria, se existir ele adiciona ao final


http://docs.python.org/3/library/funciotns.html#open

# Exemplo X

try:
    with open('universo.txt', 'x') as arquivo:
        arquivo.write('Teste.\n')
except FileExistsError:
    print('Aquivo já existe!')

# Exemplo a

with open('futras.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break


"""

with open('outro.txt', 'r+') as arquivo:
    arquivo.seek(0)
    arquivo.write('Sextou \n')
    arquivo.write('Sabadou \n')
