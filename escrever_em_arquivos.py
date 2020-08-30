"""
Escrever em arquivos

Ao abrir o arquivo para leitura não podemos realizar a escrita, apenas ler da mesma forma se abrir o arquivo para a
escrita só poderemos escrever nele.

Ao abrir um arquivo para escrita o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo utilizamos a função write.
Ela recebe uma string como parametro caso contrario teremos TypeError

Abrindo arquivo para escrita, caso ele não exista sera criado, caso já exista, o velho é apagado e um novo é criado
dessa forma todo o conteudo no aruqivo anterior é perdido.

# exemplo de escrita - Modo Write

# Forma Pythonica

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Podemos por qntos caracteres quisermos')

# Forma não Pythonica

arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.')
"""

with open('python.txt', 'w') as arquivo:
    arquivo.write('Python\n' * 10)

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break


