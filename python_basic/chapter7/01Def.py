class Person:

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