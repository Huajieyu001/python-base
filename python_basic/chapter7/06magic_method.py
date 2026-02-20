class Person:

    def __init__(self, name, age, id):
        self.name = name
        self._age = age
        self.__id = id

    def __str__(self):
        return 'name = {}, age = {}, id = {}'.format(self.name, self._age, self.__id)

    def __len__(self):
        return len(self.__dict__)

    def __lt__(self, other):
        return self._age < other._age

    def __gt__(self, other):
        return self._age > other._age

    def __eq__(self, other):
        return self._age == other._age

    def __getattr__(self, value):
        print(f'{value} is not defined')


obj = Person('lisi', 54, 5845123)
obj2 = Person('zhangsan', 65, 54516)

print(obj)
print(len(obj))
print(obj.jaja)
print(obj > obj2)
print(obj < obj2)
print(obj == obj2)
