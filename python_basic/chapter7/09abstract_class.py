from abc import ABC, abstractmethod, abstractclassmethod


class Animal(ABC):
    def speak(self):
        print("this is an animal")

    @abstractmethod
    def eat(self):
        pass

class Cat(Animal):

    def eat(self):
        print("eating meat")
# 抽象类无法实例化
# obj = Animal()
# 实现类可以
obj = Cat()
obj.speak()
obj.eat()


