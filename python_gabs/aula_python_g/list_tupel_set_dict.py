"""
eh possivel colocar qualquer tipo de dado em uma lista.

lista1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)
set1 = {1, 2, 3, 4, 5}
dict1 = {"nome": "Maria", "idade": 30}

# Lista aninhada
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lista[0])  # Saida [1, 2, 3]
print(lista[0][0])  # Saida 1
print(lista[0][1])  # Saida 5

lista[2].append(10)
lista[1].pop(-1)

print(lista)

lista1 = [[1, 2], [3, 4], [5, 6]]

for sublista in lista1:
    for elemento in sublista:
        print(elemento, end=" ")  # Saída: 1 2 3 4 5 6

print(len(lista))

biblioteca = {
    "pessoas": [
        {
        "nome": "João",
        "idade": 20
        },
        {
        "nome": "Maria",
        "idade": 25
        },
        {
        "nome": "Pedro",
        "idade": 30
        }
    ],
}

"""

di = {
    "nome": ["Maria", "Pedro", "Carla", "Gabs"],
    "idade": [30, 25, 20, 17],
}

dados = zip(di["nome"], di["idade"])
print(dict(dados))
