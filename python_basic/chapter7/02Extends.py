class Person:

    # 构造方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, message):
        print('I am {}, {} yeas, my gender is {}, message is {}'.format(self.name, self.age, self.gender, message))

    def printInfo(self):
        print('I am {}'.format(self.name))

# 继承，格式为subclass(superclass)
class Student(Person):
    def __init__(self):
        Person.__init__(self, 'Default', 0, 'Default')

    def printInfo(self):
        print("Override {}".format(self.name))

class Teacher(Person):
    pass # 可以什么都不写，使用pass来作为占位符，100%继承父类

obj1 = Person('lisi', 18, 'male')
obj2 = Student()
obj3 = Teacher('zhangsan', 24, 'female')

obj1.speak("Haha1")
obj2.speak("Haha2")
obj3.speak("Haha3")
obj1.printInfo()
obj2.printInfo() # 方法重写
obj3.printInfo()
