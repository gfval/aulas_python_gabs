""""
O método super() em Python é usado para chamar métodos da classe pai
(superclasse) dentro de uma subclasse. Ele é especialmente útil para herança,
pois permite acessar métodos da superclasse sem precisar referenciar diretamente
o nome da classe pai.

"""
# Exemplo

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"This animal says {sound}")


class Dog(Animal):
     def __init__(self, name, breed):
         super().__init__(name, species="Dog")
         self.breed = breed

     def make_sound(self, sound="Woof"):
         print(f"{self.name} says {sound}")


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed

    def make_sound(self, sound="Meow"):
        print(f"{self.name} says {sound}")


dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Siamese")

dog.make_sound()
cat.make_sound()

# Explicação:
#
# 1. A classe Animal é a superclasse que contém o método make_sound.
# 2. As classes Dog e Cat são subclasses de Animal.
# 3. O método super().__init__() é usado para chamar o construtor da classe pai
# (Animal) dentro das subclasses Dog e Cat.
# 4. O método make_sound é sobrescrito nas subclasses para fornecer
# comportamento específico para cada tipo de animal.
# 5. Quando você chama dog.make_sound() ou cat.make_sound(), o método correto
# é chamado com base no tipo de animal.
# 6. O método super() é útil para evitar a duplicação de código
# e facilitar a manutenção de classes em hierarquias de herança.
