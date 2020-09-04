"""
Teste de velocidade com expressões geradoras


"""
import time

gen_inicio = time.time()

print(sum(num for num in range(1000000000)))

gen_tempo = time.time() - gen_inicio


list_inicio = time.time()
print(sum(num for num in range(100000000)))
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou{gen_tempo}')
print(f'List Comprehension levou{list_tempo}')