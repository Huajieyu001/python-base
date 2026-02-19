
class Animal:

    def eat(self, food):
        print("eat" + food)

class Person:

    def work(self, location):
        print("I am working at {}".format(location))

# Python 支持多继承，需要自行避免菱形继承的问题
class Student(Person, Animal):
    pass

obj = Student()

obj.eat('burger')
obj.work('hospital')