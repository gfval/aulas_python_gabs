""""
modulos sao arquivos em python que contem funcoes e variaveis que podem ser
importadas de/para outros arquivos.

modulo random

from random import uniform

for i in range(10):
    print(uniform(3, 7))

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

from random import choice, shuffle
cartas = ["K", "Q", "J", "A", "2", "3", "4", "5", "6", "7"]
naipes = ["Ouros", "Paus", "Copas", "Espadas"]
print("Carta: ", choice(cartas))
print("Naipe: ", choice(naipes))
print(cartas)
shuffle(cartas)
print(cartas.pop())

"""
