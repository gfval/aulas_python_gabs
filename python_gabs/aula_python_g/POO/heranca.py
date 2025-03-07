"""
heranca tem como objetivo reutilizar código, ou seja, criar uma classe que
herda de outra classe,ou seja, a classe filha herda todos os atributos e
métodos da classe mãe.

"""


class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Veículo: {self.marca} {self.modelo}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def exibir_info(self):
        return f"Carro: {self.marca} {self.modelo}, {self.portas} portas"


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def exibir_info(self):
        return f"Moto: {self.marca} {self.modelo}, {self.cilindradas}cc"


# Criando objetos
carro1 = Carro("Toyota", "Corolla", 4)
moto1 = Moto("Honda", "CBR 600", 600)

# Exibindo informações
print(carro1.exibir_info())
print(moto1.exibir_info())
