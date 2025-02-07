"""
#Sintaxe list comprehension
[valor for valor in interavel]

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

plana = []
for lista in matriz:
    for num in lista:
        plana.append(num)
suma = sum(plana)
print(suma)

pares = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print(pares[10])

cuadrados = {x: x**2 for x in range(10)}
print(cuadrados)
# Exemplo de list comprehension para procurar elementos no dict
valores_pares = [valor for chave, valor in cuadrados.items() if valor % 2 == 0]
print(valores_pares)

a = [x for x in range(1, 101) if x % 2 != 0]
print(a)
a1 = [x for x in range(1, 11)]
print(a1)
a2 = [x for x in range(1, 21) if x % 2 == 0]
print(a2)
a3 = [x ** 2 for x in range(1, 11,)]
print(a3)


def maiuscula(a4):
    nome = a4.replace([0]), a4.upper()
    return nome


a4 = ["python", "java", "javascript", "c#", "c++"]
print(maiuscula(a4))

lista = [[1, 2, 3], [4, 5], [6]]

# Usando loop
plana1 = []
for sublista in lista:
    for elemento in sublista:
        plana1.append(elemento)


print(plana1)

# Usando list comprehension
plana = [elemento for sublista in lista for elemento in sublista]
print(plana)
total = sum(plana)

print(total)

# Sintaxe dict comprehension

{Key: value for value in interavel}

numeros = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5
}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

numeros2 = [1, 2, 3, 4, 5]
quadrado2 = {valor: valor ** 2 for valor in numeros2}
print(quadrado2)

chave = "abcde"
valor = [1, 2, 3, 4, 5]
mistura = {chave[i]: valor[i] for i in range(0, len(chave))}
print(mistura)

# Logica condicional
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = {num: ("par" if num % 2 == 0 else "impar") for num in numeros}
print(res)

# Genereator
# Sintaxe
# (valor for valor in interavel)
nome = ["Cristina", "Carlos", "Ciro", "Cleber", "Cleiton", "Cleusa", "Icaro"]
gen = (nome[0] == "C"for nome in nome)
print(gen)

gen1 = [nome for nome in id.keys() if id[nome] > 20]
print(f"A Geracao Y é: {gen1}")
"""
# Dicionário de idades
idades = {
    "Cristina": 33,
    "Carlos": 25,
    "Ciro": 18,
    "Cleber": 20,
    "Cleiton": 19,
    "Cleusa": 42,
    "Icaro": 29,
}


# Função para classificar as gerações
def classificar_geracao(dados):
    resultados = [
        f"{nome} é da Geração Y" if idade > 20 else f"{nome} é da Geração X"
        for nome, idade in dados.items()
    ]
    return resultados


# Imprimir os resultados
resultado = classificar_geracao(idades)
print("\n".join(resultado))
