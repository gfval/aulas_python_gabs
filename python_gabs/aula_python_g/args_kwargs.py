"""
ordem obrigatorios de parametros em uma função em Python
func(a, *args, b, **kwargs)

o args é um parâmetro que permite passar um número variável de argumentos para
uma função.



def soma(*args):
    total = sum(args)
    return total


print(soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(soma(4, 5, 1, 54, 5))


def exemplo(a, b, *args):
    print(f"a = {a}, b = {b}")
    print(f"args = {args}")


exemplo(1, 2, 3, 4, 5)

# desenpacotador de *args

def soma_todos_numeros(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(soma_todos_numeros(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos passando
# como argumento uma coleção de dados de dados.

# **kwargs


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f"A cor favorita de {pessoa.title()} é {cor}")


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul',
                vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()
cores_favoritas(geek='navy')

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f"{nome} tem {idade} anos")
    print(args)
    if solteiro:
        print("Solteiro")
    else:
        print("Casado")
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True,
             tulipa="De frango eh melhor", rodizio="japones")
minha_funcao(34, 'Felipe', "Eu", "prefiro", "picanha", eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

Desempacotar com **kwargs

list = [1, 2, 3]
tuple = (1, 2, 3)
set = {1, 2, 3}
dict = dict(a=1, b=2, c=3)

print(soma(*list))
print(soma(*tuple))
print(soma(*set))
print(soma(**dict))
# Os nomes da chave do dicionário devem ser os mesmos da função

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nome = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostra_nomes(**nome))

def soma(a, b, c):
    return a + b + c


# Exercicio_1
numero = float(input("Digite um número: "))


def multiplo(numero):
    total = numero * 2
    print((f'O valor da multiplicacao de {numero} com 2 eh {total}'))


multiplo(numero)

# Exercicio_2

calendario = input("Em que dd/aa/yyyy estamos? ").split("/")


def data(dia, mes, ano):
    if mes == "01":
        mes = "Janeiro"
    elif mes == "02":
        mes = "Fevereiro"
    elif mes == "03":
        mes = "Março"
    elif mes == "04":
        mes = "Abril"
    elif mes == "05":
        mes = "Maio"
    elif mes == "06":
        mes = "Junho"
    elif mes == "07":
        mes = "Julho"
    elif mes == "08":
        mes = "Agosto"
    elif mes == "09":
        mes = "Setembro"
    elif mes == "10":
        mes = "Outubro"
    elif mes == "11":
        mes = "Novembro"
    elif mes == "12":
        mes = "Dezembro"
    print(f"hoje eh {dia} de {mes} de {ano}")


data(*calendario)


# Exercicio_3
volume = float(input("Digite o raio da esfera: "))


def esfera(raio):
    return 4/3 * 3.14 * raio ** 3


print(f'O volume da esfera eh {esfera(volume)}')

"""

# Usando datetime

from datetime  import datetime
import locale

# Definir idioma para português
locale.setlocale(locale.LC_TIME, "pt_BR.utf8")

calendario = input("Em que dd/mm/yyyy estamos? ")

try:
    try:
        data_atual = datetime.strptime(calendario, "%d/%m/%Y")
    except ValueError:
        data_atual = datetime.strptime(calendario, "%m/%d/%Y")
    print(f"Hoje é {data_atual.day} de {data_atual.strftime('%B')} de {data_atual.year}")
except ValueError:
    print("Formato de data inválido! Use dd/mm/yyyy.")
