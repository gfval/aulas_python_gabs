"""


def contador():
    print("Iniciando generator...")
    yield 1
    print("Voltando para a função...")
    yield 2
    print("Finalizando generator...")
    yield 3


gen = contador()
print(next(gen))  # Iniciando generator... 1
print(next(gen))  # Voltando para a função... 2
print(next(gen))  # Finalizando generator... 3

while True:
    valor_maximo = input("Digite um número: ")
    try:
        if not valor_maximo.isdigit():
            raise ValueError("Digite um número válido!")
        valor_maximo = int(valor_maximo)
        break
    except ValueError as e:
        print(e)


def count_at(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


for numero in count_at(valor_maximo):
    print(numero)


//////////////////////////////////////////////////////////////


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for numero in fibonacci():
    if numero >= 100:
        break
print(numero)

//////////////////////////////////////////////////////////////


def buscar_registros_paginados(todos_os_registros, tamanho_pagina=10):
    for i in range(0, len(todos_os_registros), tamanho_pagina):
        yield todos_os_registros[i:i + tamanho_pagina]
        # Retorna uma "página" por vez


# Simulando um banco de dados
dados = list(range(1, 101))  # Exemplo: 100 registros

# Uso
for pagina in buscar_registros_paginados(dados, tamanho_pagina=10):
    print(pagina)  # Processa 10 registros por vez

//////////////////////////////////////////////////////////////


#  Generator
def numeros():
    for num in range(1, 11):
        yield num


gen = numeros

for num in gen():
    print(num)

#  Generator Exprecion
ge1 = (num for num in range(1, 11))
for num in ge1:
    print(num)

"""
import time

# Generator
gen_inicio = time.time()
print(sum(num for num in range(1000000001)))
gen_tempo = time.time() - gen_inicio

# List comprehension
list_inicio = time.time()
print(sum(num for num in range(1000000001)))
list_tempo = time.time() - list_inicio

print(f"O generator demorou {gen_tempo} segundos")
#  Demorou 50.41 (Usando aproximadamente 600Mb)
print(f"List comprehension demorou {list_tempo} segundos")
#  Demorou 663.70(Usando 13Gb de memoria)
