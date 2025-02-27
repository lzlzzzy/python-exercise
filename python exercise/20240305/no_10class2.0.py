#使用类和实例，可使用类来模拟现实世界中的很大情景。

#下面来编写一个表示汽车的类
class Car:
    def __init__(self,make,model,year):
        self.make=make        #初始化描述汽车的属性
        self.model=model
        self.year=year
#2创建实例时，有些属性无须通过形参来定义，可在方法__init__()中为其指定默认值
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
#2打印一条指出汽车里程的消息
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

my_new_car=Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()




