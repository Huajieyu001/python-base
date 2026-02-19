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

    # 类方法（使用@classmethod注解即可）
    @classmethod
    def test1(cls):
        print('This is test1')
        print(cls)
        print(type(cls))

    @classmethod
    def test2(cls, data):
        print('This is test2')
        print(f'your data is {data}')

    @classmethod
    def setMaxAge(cls, age):
        cls.max_age = age

    @classmethod
    def getMaxAge(cls):
        return cls.max_age

    @classmethod
    def setPlanet(cls, planet):
        cls.planet = planet

    @classmethod
    def getPlanet(cls):
        return cls.planet

    @classmethod
    def create(cls, info):
        name, age, gender = info.split('-')
        age = int(age)
        return Person(name, age, gender)

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
# 调用类方法
Person.test1()
Person.test2(45)
obj1.test1() # 通过实例调用类方法也没问题
print('-' * 30)
# 使用工厂方法
p = Person.create('zhangsan-18-male')
print(p.getName())
print(p.getAge())
print(p.getGender())