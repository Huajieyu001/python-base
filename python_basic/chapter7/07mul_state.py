class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("this is an animal")


class Dog(Animal):

    def speak(self):
        print("this is a dog")


class Cat(Animal):
    def speak(self):
        print("this is a cat")


def speak(animal: Animal):
    animal.speak()

speak(Dog('Tom', 54))
speak(Cat('Dop', 651))
speak(Animal('Sad', 8))