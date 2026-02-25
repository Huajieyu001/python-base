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
# 判断arg1是不是arg2的实例对象或者子类实例对象
print(isinstance(obj, Student))
print(isinstance(obj, Animal))
print(isinstance(obj, Person))
# 判断arg1是不是arg2的子类
print(issubclass(Student, Person))
print(issubclass(Student, Animal))
print(issubclass(Person, Student))
