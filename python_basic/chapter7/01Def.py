class Person:

    # 类属性
    max_age = 120
    planet = 'Earth'

    # 构造方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getGender(self):
        return self.gender

    def setGender(self, gender):
        self.gender = gender

    def toString(self):
        return str(self.name) + "," + str(self.age) + "," + str(self.gender)

    # 类方法
    # def

# 创建实例
obj1 = Person("zhangsan", 21, "Male")
obj2 = Person("lisi", 22, "Female")

print(obj1)
print(obj1.toString())
print(type(obj1))
print(obj1.getName())
print(obj1.getAge())
print(obj1.getGender())
# 获取实例所有属性（dict）
print(obj1.__dict__)
# 获取类的所有属性
print(Person.__dict__)
print(Person.max_age)
print(Person.planet)
Person.max_age = 100
Person.planet = 'Mars'
print(Person.max_age)
print(Person.planet)

obj1.max_age = 0
print(obj1.max_age) # 通过实例.变量的方式修改类属性，只对实例自身有用，不会影响到类
print(Person.max_age)

# 通过实例调用实例方法
print(obj1.getName())
# 通过类调用实例方法，通过类调用时，self需要自己传入实例对象，如果通过实例对象调用则无需自行传入self
print(Person.getName(obj1))