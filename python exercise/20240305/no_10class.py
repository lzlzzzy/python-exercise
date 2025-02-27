#在python中，Dog首字母大写的名称指的是类
# __init__的函数称为方法，每当我根据Dog类创建新实例时，python都会主动运行它
class Dog:
    def __init__(self,name,age):
        self.name=name          #self.name=name获取与形参name相关联的值，并将其赋给变量name，然后该变量被关联到当前创建的实例。
        self.age=age
    def sit(self):
        print(f"{self.name} is now sitting")
    def roll_over(self):
        print(f"{self.name} rolled over")

my_dog=Dog('tom',6)
print(f"My dog name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
#访问属性,可用句号表示法,在这里，python先找到实例my_dog，在查找与该实例相关联的属性name，在Dog类中引用这个属性时，使用的是self.name
#调用方法
my_dog.sit()
my_dog.roll_over()

your_dog=Dog("lucy",3)
print(f"Your dog name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()

