"""
Nomes de class devem ser em CamelCase(toda via classes internas do python
devem ser em snake_case ou sem letras maiusculas).

pass: é uma palavra reservada que é usada quando queremos criar uma classe
vazia, ou seja, sem nenhum atributo ou método.


Exemplo 1: Classe Simples
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("João", 30)
print(pessoa1.cumprimentar())

Descrição:

@staticmethod define um método estático que não depende de nenhuma instância
da classe.
@classmethod define um método de classe que recebe a própria classe (cls) como
primeiro argumento.
Matematica.somar(5, 3) chama o método estático somar.
Matematica.multiplicar(5, 3) chama o método de classe multiplicar.

"""


#  Exemplo:
class MinhaClasse:
    pass
