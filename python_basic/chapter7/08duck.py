class Dog:
    def speak(self):
        print("this is a dog")


class Cat:
    def speak(self):
        print("this is a cat")

class Pig:
    def speak(self):
        print("this is a pig")

# 鸭子多态
def speak(animal):
    animal.speak()

speak(Dog())
speak(Cat())
speak(Pig())