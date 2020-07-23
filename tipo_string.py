"""
Tipo String

Em Python um dado é considerado do tipo string sempre que:

- Estiver entre àspas simple -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Teste de String'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \n Jolie'
print(nome)
print(type(nome))

Considerando caracter de escape \
nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

print(nome.split()) # Transforma em uma lista de strings

print(nome.upper())

print(nome.lower())
"""
# Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

# ['U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y', ' ', 'T', 'u', 't', 'o', 'r', 'i', 'a', 'l', 's']
nome = 'University Tutorials'
print(nome[0:4])    # Slice de string

print(nome[5:15])   # Slice de string

print(nome[0:1])    # valor precisa ser definido até o próximo caracter

print(nome.split()[1])

print(nome[14], nome[13])

print(nome[::-1])   # Inversão da String Pythonico

print(nome.replace('i', 'P'))

texto = 'socorram me subindo onibus em marrocos' # Palíndromo

print(texto)

print(texto[::-1])