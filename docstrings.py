"""
Documentando funções com Docstrings

Podemos ter acesso a doc de uma func em Python usando a propriedade __doc__

Podemos ainda fazer acesso a documentação com a função help()


"""

# Exemplo

def diz_oi():
    """ Uma função simples que retorna a string Oi"""
    return 'oi!'


def exponencial(numero, potencial=2):
    """
    Função que retorna por padrão o quadrado de "numero" ou o 'numero' ou a potencia informada
    :param numero: Numero que desejamos gerar o exponencial
    :param potencial: Potencia que queremos gerar o exponencial por padrão 2
    :return: retorna o exponencial de numero por potencia
    """
    return numero ** potencial

