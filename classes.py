from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def rando(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, is a: {self.breed}"

    def rando(self):
        pass

    def speak(self):
        return "Bark"


dog1 = Dog("Fido", 3, "Pug")
dog2 = Dog("Sally", 6, "Pomeranian")
print(dog1.name)
print(dog2.rando())