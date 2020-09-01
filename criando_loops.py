"""
Criando sua propria versão de loops


for num in [1, 2, 3, 4, 5]:
    print(num)
"""

def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Python')

numeros = [1, 2, 3, 4, 5]

meu_for(numeros)