"""
open() -> é uma função integrada do Python usada para abrir um arquivo
ou uma URL.
open() -> retorna um objeto do tipo arquivo que pode ser usado para ler,
gravar e manipular o arquivo.

arquivo = open('text.txt')
print(arquivo)
print(type(arquivo))
print(arquivo.read())
print(arquivo.read(30)) -> vai ler 30 caracteres.

//////////////////////////////////////////////////
seek() -> é utilizado para movimentar o cursor pelo arquivo.
| -> cursor ou seek do arquivo.
EX:
arquivo = open('text.txt')
print(arquivo.read())
サイバー|
seek(0)
# movimenta o cursor para o indice 0 do arquivo.
|サイバー

//////////////////////////////////////////////////
readline() -> lê o arquivo linha a linha.
EX:
arquivo = open('text.txt')
print(arquivo.readline())
ヘロー・
print(arquivo.readline())
サイバー・
print(arquivo.readline())
プリーズ・

readlines() -> lê o arquivo linha a linha e armazena em uma lista.
EX:
arquivo = open('text.txt')
linhas = arquivo.readlines()
print(linhas)
print(len(linhas))
for linha in linhas:
    print(linha)

//////////////////////////////////////////////////
close() -> fecha o arquivo. Após o uso do arquivo, é uma boa prática.
EX:
arquivo = open('text.txt')
print(arquivo.read())
arquivo.close()
print(arquivo.closed) # True -> arquivo fechado.

/////////////////////////////////////////////////
Bloco with
# O bloco with é utilizado para criar um contexto de uso do arquivo,
# garantindo que ele será fechado corretamente após o uso.
# EX:
with open('text.txt') as arquivo:
    print(arquivo.read())
# O arquivo é fechado automaticamente ao sair do bloco with.
print(arquivo.closed)  # True -> arquivo fechado.

//////////////////////////////////////////////////
r ->Abre para leitura
w ->Abre para sobre escrever - sobre escreve caso o arquivo ja exista
x ->Abre para escrita somente se o aquivo nao existir
a ->Abre para a escrita, adicionando o conteudo ao final do arquivo

/////////////////////////////////////////////////
Abrindo arquivos para sobre escerever
# OBS:ao abrirmos um arquivo para escrita nao podemos ler o mesmo e vice versa.
# Para escrever em um arquivos deve ser passado o parametro "w"(write)
# EX:
with open("text.txt", "w") as arquivo
    arquivo.write("eh possivel adicionar"\n)
    arquivo.write("elementos ao arquivo"\n)
    arquivo.write("dessa forma.")

Recebendo dados:

obj = (
    "carro",
    "mesa",
    "computador",
    "tela"
    )

with open("fruta.txt", "a") as arquivo:
    while True:
        fruta = input("informe uma fruta:")
        if fruta in obj:
            raise ValueError("Digite uma fruta, nao um numero")
        elif fruta == int or float:
            raise ValueError("Digite uma fruta, nao um numero")
        elif fruta != "sair" or "Sair":
            arquivo.write(fruta + "\n")
        else:
            break

///////////////////////////////////////////////////
StringIO

Para ler ou escrever dados em arquivos do sistema operacional o software
precisa ter permisao:
    -Permissao de leitura ->Para ler o arquivo.
    -Permissao de escrita ->Para escrever no arquivo.

StringIO - Ultilizado para ler e criar arquivos em memoria.

from io import StringIO

mensagem = "essa eh apenas uma string comum."

arquivo = StringIO(mensagem)

print(arquivo.read())

arquivo.write("Mais texto.")

arquivo.seek(0)

print(arquivo.read())

"""
