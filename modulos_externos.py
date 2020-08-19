"""
Módulos externos

Utilizamos o gerenciador de pacotes python chamado Pip - Python installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal

from colorama import init, Fore

init()

print(Fore.YELLOW + 'Python')


"""

import pydf

pdf = pydf.generate_pdf('<h1>Python</h1>')

with open('teste_doc.pdf', 'wb') as f:
    f.write(pdf)

