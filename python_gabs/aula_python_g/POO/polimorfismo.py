"""

"""
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"

def animal_sound(animal):
    print(animal.speak())

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

animal_sound(dog)
animal_sound(cat)
animal_sound(cow)
