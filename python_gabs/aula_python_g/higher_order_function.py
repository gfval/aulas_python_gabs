"""
First Class Function

def somar(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a / b

def calculo(a, b, function):
    return function(num1, num2)

"""
# Nested Function

from random import choice

amigos = ("Cristian", "Patrick", "Matheus")


def comprimento(pessoa):
    def humor():  # Uma nested function(Uma funcao dentro de outra)
        return choice(("Eai ", "Se manca ", "Oii, como vc ta? "))
    return humor() + pessoa


for pessoa in amigos:
    print(comprimento(pessoa))


# Retornando funcoes de outras funcoes
def risada():
    def rir():
        return choice(("kkkkkkkkkk", "hahahahahahah", "kakakakaka"))
    return rir


rindo = risada()
print(rindo())
