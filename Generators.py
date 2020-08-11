"""
Generators

# Usando generators

nomes = ['Carlos', 'Camila']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension

res = [nome[0] == 'C' for nome in nomes]
print(res)

# Qual a função? Retorna a quantidade de bytes passado em parametros na memoria.
from sys import getsizeof

print(getsizeof('Geek'))

from sys import getsizeof

list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastmos em memoria: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dict Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')

"""

# eu posso iterar no Generator Expression ? Yes

gen = (x * 10 for x in range(1000))

for num in gen:
    print(num)
