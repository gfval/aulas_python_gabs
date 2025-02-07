def diz_oi():
    """
    Função simples que retorna a string 'Oi!'
    """
    return 'Oi!'


print(diz_oi.__doc__)


def exponencial(numero, potencia=2):
    """
    Função que retorna um número elevado a uma potência
    :param numero: int ou float
    :param potencia: int ou float
    :return: int ou float
    """
    return numero ** potencia
