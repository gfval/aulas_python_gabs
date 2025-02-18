"""
Decorators em Python são uma maneira de modificar ou estender o comportamento
de funções ou métodos sem alterar seu código. Eles são funções que recebem
outra função como argumento e retornam uma nova função que geralmente estende
o comportamento da função original.

Aqui está um exemplo simples de um decorator:

def meu_decorator(func):
    def wrapper():
        print("Algo está acontecendo antes da função ser chamada.")
        func()
        print("Algo está acontecendo depois da função ser chamada.")
    return wrapper

@meu_decorator
def diz_oi():
    print("Oi!")

diz_oi()

Algo está acontecendo antes da função ser chamada.
Oi!
Algo está acontecendo depois da função ser chamada.

1.meu_decorator é um decorator que recebe a função diz_oi como argumento.
2.Dentro de meu_decorator, a função wrapper é definida para adicionar
comportamento antes e depois da chamada da função original.
3.O decorator é aplicado à função diz_oi usando a sintaxe @meu_decorator.
4.Quando diz_oi é chamada, o comportamento adicional definido em wrapper é
executado antes e depois da chamada da função original.

Explicacao:

O símbolo @ em Python é usado para aplicar decorators a funções ou métodos.
Quando você coloca @decorator_name acima de uma função, está dizendo ao Python
para passar essa função como argumento para o decorator.

# Exemplo mais complexo


class Circulo:
    def __init__(self, raio):
        self._raio = raio

    @property
    def raio(self):
        return self._raio

    @raio.setter
    def raio(self, valor):
        if valor < 0:
            raise ValueError("O raio não pode ser negativo")
        self._raio = valor

    @property
    def area(self):
        import math
        return math.pi * (self._raio ** 2)


# Uso do decorator @property
circulo = Circulo(5)
print(circulo.raio)  # Acessa o método raio como um atributo
print(circulo.area)  # Acessa o método area como um atributo

circulo.raio = 10  # Usa o setter para modificar o valor do raio
print(circulo.area)  # Acessa o método area como um atributo

# Tentar definir um raio negativo gera um erro
try:
    circulo.raio = -5
except ValueError as e:
    print(e)

# A saída será:
# 5
# 78.53981633974483
# 314.1592653589793
# O raio não pode ser negativo

"""
from functools import wraps

tempo = input("Está com pressa? (Sim/Não): ").strip().lower()
pressa = tempo == "sim"


def fome(funct):
    @wraps(funct)
    def mal_educado(*args, **kwargs):
        return funct(*args, **kwargs) + " AGORA!".upper()
    return mal_educado if pressa else funct


def gritar(funct):
    @wraps(funct)
    def aumentar(*args, **kwargs):
        return funct(*args, **kwargs).upper()
    return aumentar if pressa else funct


@gritar
@fome
def pedido(principal, acompanhamento):
    return f"Vou querer {principal} com {acompanhamento}."


print(pedido("frango", "batata assada"))
print(pedido(principal="Peito de Frango", acompanhamento="Fritas"))
print(1) if pressa else print(0)
