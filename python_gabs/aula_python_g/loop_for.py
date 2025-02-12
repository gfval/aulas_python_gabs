"""
nome = "Gabis"
lista = [1, 2, 3, 4, 5]
numero = range(1, 10)
for letra in nome:
    print(letra)
for numero in lista:
    print(numero)


"""

respostas_incorretas = (
    "Homem",
    "homem",
    "Macho",
    "macho"
    )

while True:
    ptrk = input("Qual o gênero do Patrik? ")
    if ptrk in respostas_incorretas:
        print("Incorrecto")
    else:
        print("Correcto")
        break
