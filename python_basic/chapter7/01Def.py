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
