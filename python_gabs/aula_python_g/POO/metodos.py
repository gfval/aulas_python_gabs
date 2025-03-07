"""
No python existem metodos de instancia e metodos de classe.

"""


# Métodos são funções que pertencem a uma classe
class conta:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.__conta__saldo = saldo


c = conta("João", 100)
c.__conta__saldo = 200
#  print(c._conta_saldo)
print(dir(c))
