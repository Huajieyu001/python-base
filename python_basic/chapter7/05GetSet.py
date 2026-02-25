class Person:

    def __init__(self, name, age, id):
        self.name = name
        self._age = age
        self.__id = id

    # getter
    @property
    def age(self):
        return self._age

    # setter
    @age.setter
    def age(self, age):
        self._age = age

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

p = Person('John', 23, 68412241321321)
print(p.name)
print(p.age)
print(p.id)

p.age = 8888
p.id = 888888888888888888
print(p.name)
print(p.age)
print(p.id)