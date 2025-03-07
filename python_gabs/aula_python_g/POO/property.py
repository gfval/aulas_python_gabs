"""
Em Python, podemos usar @property para criar atributos que funcionam como
métodos, permitindo validação ou processamento antes de serem acessados ou
modificados.

"""


class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca  # Atributo privado (indicado por _)
        self._modelo = modelo

    @property  # Getter
    def marca(self):
        return self._marca

    @marca.setter  # Setter
    def marca(self, nova_marca):
        if isinstance(nova_marca, str) and nova_marca.strip():
            self._marca = nova_marca
        else:
            raise ValueError("Marca inválida!")

    @property  # Getter
    def modelo(self):
        return self._modelo

    @modelo.setter  # Setter
    def modelo(self, novo_modelo):
        if isinstance(novo_modelo, str) and novo_modelo.strip():
            self._modelo = novo_modelo
        else:
            raise ValueError("Modelo inválido!")

    def exibir_info(self):
        return f"Veículo: {self.marca} {self.modelo}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas

    @property  # Getter
    def portas(self):
        return self._portas

    @portas.setter  # Setter
    def portas(self, quantidade):
        if isinstance(quantidade, int) and quantidade > 0:
            self._portas = quantidade
        else:
            raise ValueError("Número de portas inválido!")

    def exibir_info(self):
        return f"Carro: {self.marca} {self.modelo}, {self.portas} portas"


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self._cilindradas = cilindradas

    @property  # Getter
    def cilindradas(self):
        return self._cilindradas

    @cilindradas.setter  # Setter
    def cilindradas(self, valor):
        if isinstance(valor, int) and valor > 50:
            self._cilindradas = valor
        else:
            raise ValueError("Cilindrada inválida!")

    def exibir_info(self):
        return f"Moto: {self.marca} {self.modelo}, {self.cilindradas}cc"


# Criando objetos
carro1 = Carro("Toyota", "Corolla", 4)
moto1 = Moto("Honda", "CBR 600", 600)

# Exibindo informações
print(carro1.exibir_info())  # Saída: Carro: Toyota Corolla, 4 portas
print(moto1.exibir_info())  # Saída: Moto: Honda CBR 600, 600cc

# Testando setters e validações
carro1.portas = 2  # Modifica o número de portas
moto1.cilindradas = 1000  # Modifica a cilindrada

print(carro1.exibir_info())  # Saída: Carro: Toyota Corolla, 2 portas
print(moto1.exibir_info())  # Saída: Moto: Honda CBR 600, 1000cc

# Testando validação
try:
    moto1.cilindradas = 30  # Erro! Cilindrada inválida
except ValueError as e:
    print(e)  # Saída: Cilindrada inválida!
