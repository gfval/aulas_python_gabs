"""
Manipulação de Diretórios e Arquivos

Comando                   |    Descrição

os.getcwd()	              | Retorna o diretório atual.
os.chdir(caminho)	      | Altera o diretório de trabalho.
os.listdir(caminho)       | Lista os arquivos e pastas em um diretório.
os.mkdir(nome_pasta)      | Cria um novo diretório.
os.makedirs(caminho)	  | Cria diretórios recursivamente.
os.rmdir(nome_pasta)	  | Remove um diretório vazio.
os.removedirs(caminho)	  | Remove diretórios recursivamente.
os.remove(nome_arquivo)	  | Deleta um arquivo.
os.rename(origem, destino)|	Renomeia ou move um arquivo/pasta.

/////////////////////////////////////////////////////////////////////////////////////
Informações do Sistema

Comando         |	Descrição

os.name         |	Retorna o nome do sistema operacional
                |    ('posix' para Linux/Mac,'nt' para Windows).
os.uname()      |	Retorna informações sobre o sistema (Linux/Mac).
os.environ      |	Retorna variáveis de ambiente.
os.getenv('VAR')|	Obtém o valor de uma variável de ambiente.
os.cpu_count()  |	Retorna o número de CPUs disponíveis.

/////////////////////////////////////////////////////////////////////////////////////
Permissões e Propriedades de Arquivos

Comando                    |	Descrição

os.chmod(caminho, modo)    |	Altera as permissões de um arquivo.
os.stat(caminho)           |	Retorna informações sobre um arquivo.
os.access(caminho, modo)   |	Verifica permissões de acesso
                           |     (os.R_OK, os.W_OK,os.X_OK).

/////////////////////////////////////////////////////////////////////////////////////
Caminhos e Diretórios (Usando os.path)

Comando                     |	Descrição

os.path.join(p1, p2)	    |   Junta caminhos de forma segura.
os.path.exists(caminho)     |	Verifica se um arquivo ou pasta existe.
os.path.isfile(caminho)     |	Verifica se é um arquivo.
os.path.isdir(caminho)      |	Verifica se é um diretório.
os.path.basename(caminho)	|   Retorna o nome do arquivo.
os.path.dirname(caminho)	|   Retorna o diretório do arquivo.
os.path.abspath(caminho)	|   Retorna o caminho absoluto.
os.path.getsize(caminho)	|   Retorna o tamanho de um arquivo.

////////////////////////////////////////////////////////////////////////////////////
# Obtendo diretório atual
print("Diretório atual:", os.getcwd())

# Criando uma pasta
os.mkdir("nova_pasta")

# Listando arquivos no diretório atual
print("Arquivos na pasta:", os.listdir("."))

# Removendo a pasta criada
os.rmdir("nova_pasta")

print(os.environ)
os.getenv("ALLUSERSPROFILE")
print(os.getenv("ALLUSERSPROFILE"))

# Descobrindo se um arquivo ou diretorio existe.
print(os.path.exists("text.txt"))  # False

# Path relativo
relative_path = os.path.abspath(
    "aulas_python_gabs\\python_gabs\\aula_python_g"
)
print(os.path.exists(relative_path))  # False

# Path absoluto
absolute_path =
"C:\\Users\\Val\\Documents\\GitHub\\aulas_python_gabs\\python_gabs\\aula_python_g"
print(os.path.exists(absolute_path))  # True

////////////////////////////////////////////////////////////////////////////////////
import os
from pathlib import Path

#  Nao funciona em windows
os.mknod("Nome_do_aqruivo.txt", "w")
os.mknod("C:\\User\\Val\\Documents\\GitHub\\aulas_python_gabs.txt", "w")

#  Para Windows e outros
with open("Novo_arquivo2.txt", "w") as arquivo:
    pass

#  Ou
open("Novo_arquivo3.txt", "w").close()

#  Ou usando pathlib
Path("Novo_arquivo4").touch()

os.makedirs("teste1\\tenta\\tiva")
with open("teste1\\tenta\\tiva", "w") as T1:
    T1.write("Hello word!")

#  Arquivos e diretorios temporarios
import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f"Arquivo temporario criado em {tmp}")
    with open(os.path.join(tmp, "arquivo_temporario.txt"), "w") as arquivo:
        arquivo.write("Primeito temp\n")
    input()

#  Assim que o script sair do with os arquivos sao deletados.

"""
