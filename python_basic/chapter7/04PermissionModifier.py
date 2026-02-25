
class Person:

    def __init__(self, name, age, id):
        self.name = name
        self._age = age
        self.__id = id

    @property
    def age(self):
        return self._age

    def getInfo1(self):
        print(self.name, self._age, self.__id)

class Student(Person):
    def getInfo2(self):
        print(self.name, self._age) # self.__id访问报错'Student' object has no attribute '_Student__id'

obj1 = Person('Tom', 20, 9527)
obj1.getInfo1()

obj2 = Student('Rosy', 18, 8444)
obj2.getInfo2()

print(obj1._Person__id)
