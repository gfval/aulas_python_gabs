""""
Erros e execeções são a mesma coisa
Erros Mais comuns em Python:

1)SintaxeError:
    - Erro de sintaxe, ocorre quando o interpretador não consegue interpretar
    o código.
    - Ou seja o código não está escrito de forma correta.
    Exemplo:
    A)
    def funcao:
        print('Olá, Mundo!')

    B)
    def = 1

    C)
    return

2) NameError:
    - Ocorre quando uma variável ou função não foi definida.
    Exemplo:
    A)
    print(a)

    B)
    print(nome)

3) TypeError:
    - Ocorre quando uma função é aplicada a um tipo de dado incompatível.
    Exemplo:
    A)
    print(len(5))

    B)
    print('Olá' + 5)

4) IndexError:
    - Ocorre quando tentamos acessar um índice que não existe.
    Exemplo:
    A)
    lista = [1, 2, 3]
    print(lista[3])

    B)lista = ["geeke", "university"]
    print(lista[0][])

5) ValueError:
    - Ocorre quando uma função recebe um argumento com tipo correto,
    mas valor inapropriado.
    Exemplo:
    A)
    print(int('A'))

    B)
    print(int('10.5'))

6) KeyError:
    - Ocorre quando tentamos acessar um elemento de um dict que não existe.
    - Ou quando tentamos acessar um elemento de um dict sem a chave.
    Exemplo:
    A)
    dict = {'nome': 'Gabs'}
    print(dict['idade'])

    B)
    di = {'nome': 'Gabs'}
    print(di[0])

7) AttributeError:
    - Ocorre quando tentamos acessar um atributo ou método que não existe.
    Exemplo:
    A)
    lista = [1, 2, 3]
    lista.push(4)

    B)
    lista = [1, 2, 3]
    lista.append(4)

8) IndentationError:
    - Ocorre quando a identação do código não está correta.
    Exemplo:
    A)
    def funcao():
    print('Olá, Mundo!')

    B)
    if True:
    print('Olá, Mundo!')

9) UnboundLocalError:
    - Ocorre quando tentamos acessar uma variável local que não foi definida.
    Exemplo:
    A)
    def funcao():
        print(a)
        a = 10

    B)
    def funcao():
        print(a)
        a = 10

10) ZeroDivisionError:
    - Ocorre quando tentamos dividir um número por zero.
    Exemplo:
    A)
    print(10/0)

    B)
    print(10/0)

11) FileNotFoundError:
    - Ocorre quando tentamos abrir um arquivo que não existe.
    Exemplo:
    A)
    arquivo = open('arquivo.txt', 'r')

    B)
    arquivo = open('arquivo.txt', 'r')

12) ModuleNotFoundError:
    - Ocorre quando tentamos importar um módulo que não existe.
    Exemplo:
    A)
    import moduloinexistente

    B)
    import moduloinexistente

13) ImportError:
    - Ocorre quando ocorre um erro ao importar um módulo.
    Exemplo:
    A)
    from math import inexistente

    B)
    from math import inexistente

14) KeyboardInterrupt:
    - Ocorre quando o usuário interrompe a execução do programa.
    - Pressionando Ctrl + C.
    Exemplo:
    A)
    while True:
        pass

    B)
    while True:
        pass

15) RecursionError:
    - Ocorre quando a recursão excede o limite.
    Exemplo:
    A)
    def funcao():
        funcao()

    B)
    def funcao():
        funcao()

16) MemoryError:
    - Ocorre quando o programa ultrapassa a quantidade de memória disponível.
    Exemplo:
    A)
    lista = []
    while True:
        lista.append('Olá')

    B)
    lista = []
    while True:
        lista.append('Olá')

17) AssertionError:
    - Ocorre quando uma expressão assert falha.
    Exemplo:
    A)
    assert 1 == 2

    B)
    assert 1 == 2

////////////////////////////////////////////////////////////////////////////////////////////////////

Tratamento de Erros com Try, Except:
Raise:
    - Podemos lançar exceções em Python usando a palavra-chave raise.
    - Podemos lançar exceções de qualquer tipo.
    - Podemos criar nossas próprias exceções.
    Exemplo:
    A)
    raise ValueError('Valor inválido')

    B)
    raise TypeError('Tipo de dado inválido')
    C)
    def cores(texto, cor):
    cores = {
        'vermelho': '\033[91m',
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'azul': '\033[94m',
        'roxo': '\033[95m',
        'ciano': '\033[96m',
        'sem_cor': '\033[0m'
    }

    if cor not in cores:
        raise ValueError('Cor inválida')
    print(f'{cores[cor]}{texto}{cores["sem_cor"]}')

OBS:O raise finaliza função, ou seja, se houver código após o raise,
ele não será executado.

////////////////////////////////////////////////////////////////////////////////////////////////////

Try, Except, Else, Finally:
# Try nao é a melhor forma de tratar um erro de execução ou de logica
# e que seja esperado.
# Mas podemos evitar erros inesperados e esperados no codigo.
            # Uso indevido do try.
Sintaxe:
try:
    # Código que pode gerar um erro
    except:
    # Código que será executado caso ocorra um erro
    else:
    # Código que será executado caso não ocorra um erro
    finally:
    # Código que será executado sempre

Exemplo:

try:
    geek()
except:
    print('Deu erro')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


doc = {
    'nome': 'Gabs'
    }

print(pega_valor(doc, 'nome'))
# Saida: Gabs
print(pega_valor(doc, 'idade'))
# KeyError Saida: None
print(pega_valor(8, [1]))
# TypeError Saida: None

TODA ENTRADA DEVE SER TRATADA.

while num := str:
    try:
        num = float(input('Digite um número: '))
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
    else:
        print(f'Você digitou {num}')
        break


while num := str:
    try:
        num = float(input('Digite um número: '))
    except ValueError:
        print('Digite um numero valido nao uma letra.')
    except KeyboardInterrupt:
        print('Você interrompeu a execução')
        break
    except Exception as e:
        print(f'Erro inesperado: {e}')
    else:
        print(f'Você digitou {num}')
    break

"""
