"""
list -> eh definida usando []
colecao mutavel e ordenada de elementos

# Exemplo de lista
minha_lista = [1, 2, 3, "texto", True]

tuple -> eh definida usando ()
colecao imutavel e ordenada de elementos

# Exemplo de tuple
minha_tupla = (1, 2, 3, "texto", True)
outra_tupla = 1, 2, 3  # Também é uma tupla

set -> eh definida usando {}
colecao mutavel, nao ordenada de elementos e sem elementos duplicados

dict -> eh definida usando {}
colecao mutavel, nao ordenada de pares chave-valor

# Exemplo de dict
meu_dicionario = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

a = [1, 2, 3, 4]  # list
b = (1, 2, 3, 4)  # tuple
c = {1, 2, 3, 4}  # set
d = {"nome": "Maria", "idade": 30}  # dict
"""

"""
def saudacao(nome: str):
    print(f"Olá, {nome}!")

saudacao("João")  # Saída: Olá, João!
saudacao("Maria")  # Saída: Olá, Maria!

def multiplicar(a, b):
    return a ** b

print(multiplicar(3, 4))  # Saída: 12
print(multiplicar(-1, 2))  # Saída: -2
"""


def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")


saudacao()           # Saída: Olá, Visitante!
saudacao("Carlos")   # Saída: Olá, Carlos!


def apresentar(nome: str, idade: int):
    print(f"Nome: {nome}, Idade: {idade}")


apresentar(idade=30, nome="Ana")  # Saída: Nome: Ana, Idade: 30
