"""
Definindo funções

- Funções são pequenas partes de código que realizam tarefas especificas;
- pode ou não receber entradas de dados e retornar uma saida de dados;
- muito uteis para executar procedimentos similares por repetidas vezes;

OBS.: se vc escrever uma função que realiza varias tareffas dentro dela: é bom fazer uma
verificação para que a função seja simplificada.

Já utilizamos varias funções desde que iniciamos este curso
- print()
- len()
- max()
- min()
- count()
- e muitas outras

"""

# Exemplo de utilização de funções:

#cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do python

#print(cores)

#cores.append('roxo')

#print(cores)

# Como definir funções

"""
Em python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao


Onde:

nome_da_funcao -> sempre com letras minusculas e se for nome composto separado por underline(Snake case):
parametros_de_entrada -> Opcionais onde tendo mais de um cada um separado por virgula opcional ou não.
bloco_da_funcao -> tambem chamado de corpo da função ou implementação é onde o processamento acontece
neste bloco pode ou não retorno da função. 

OBS.: Veja que para definir uma função utiizamos a palavra reservada 'def' informado ao Python
que estamos definindo uma função. Também abrimos o bloco de código com o : que é utiliza em Python
para definir blocos
"""

# Definindo a primeira função


def diz_oi():
    print('oi!')


"""
OBS.:

1 - Veja que dentor das nossas funções podemos utilizar outras funções
2 - Veja que nossa função só executa 1 tarefa, ou seja, a unica coisa que ela faz é dizer Oi
3 - Veja que esta função não recebe parametro de entrada 
4 - Veja que esta função nçao retorna nada
"""

# utilizar a função

# diz_oi()


"""
Atenção, não esqueça de utilizar o parenteses ao executar uma função
"""

# Exemplo 2

def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o Aniversariante')

# for n in range(5):
#    cantar_parabens()


# Em Python podemos inclusive criar variaves do tipo de uma função e executar a função atraves dela

canta = cantar_parabens

canta()