"""
Atributos são características de um objeto. Eles são definidos na classe e
podem ser acessados e modificados através de métodos.

Em python, dividimos os atributos em 3 tipos:
    - Atributos de instância
    - Atributos de classe
    - Atributos privados

Atributos de instância:
    - São atributos que pertencem a uma instância específica da classe.
    - Eles são definidos dentro do método __init__.
    - Eles são acessados e modificados através de métodos.
    - Eles são acessados e modificados diretamente através do objeto.
    - Eles são acessados e modificados diretamente através da classe.

Atributos de classe:
    - São atributos que pertencem a classe.
    - Eles são definidos fora dos métodos.
    - Eles são acessados e modificados através da classe.
    - Eles são acessados e modificados através do objeto.

Atributos privados:
    - São atributos que não devem ser acessados ou modificados diretamente.
    - Eles são definidos com dois underlines no início do nome (__nome).
    - Eles são acessados e modificados através de métodos.
    - Eles são acessados e modificados diretamente através do objeto(dentro da
    mesma classe).

"""


class lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.cor = cor
        self.voltagem = voltagem
        self.luminosidade = luminosidade
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, agencia, saldo):
        self.__numero = numero
        self.agencia = agencia
        self.__saldo = saldo


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


class Usuario:
    """
    A class used to represent a User.
    Attributes
    ----------
    nome : str
        The name of the user.
    email : str
        The email address of the user.
    senha : str
        The password of the user.
    __acesso : bool
        A private attribute that indicates whether the user has access.
    Methods
    -------
    login(email, senha)
        Verifies the user's email and password to grant access.
    status_acesso()
        Returns the current access status of the user.
    """
    """
    Parameters
    ----------
    nome : str
        The name of the user.
    email : str
        The email address of the user.
    senha : str
        The password of the user.
    """
    """
    Verifies the user's email and password to grant access.
    Parameters
    ----------
    email : str
        The email address of the user.
    senha : str
        The password of the user.
    Returns
    -------
    str
        A message indicating whether access is granted or denied.
    """
    """
    Returns the current access status of the user.
    Returns
    -------
    bool
        The current access status of the user.
    """

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.__acesso = False

    def login(self, email, senha):
        if self.email == email and self.senha == senha:
            self.__acesso = True
            return "Acesso permitido"
        else:
            self.__acesso = False
            return "Acesso negado"

    def status_acesso(self):
        return self.__acesso


User = Usuario("Gabs", "User@gmail.com", "123456")
# Instanciando um objeto da classe Usuario
email = input("Digite seu email: ")
senha = input("Digite sua senha: ")
print(User.login(email, senha))
print(f"Email: {User.email}, Acesso: {User.status_acesso()}")
