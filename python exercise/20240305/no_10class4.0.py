# 继承，编写类时，并非总是要从空白开始，如果要编写的类是另一个现成类的”特殊版本“，可使用继承，
# 一个类继承另一个类时，将自动获得另一个类的所有属性和方法，同时也可以定义自己的属性和方法。原有是父类，新类是子类，父类：superclass
class Car:
    def __init__(self,make,model,year):
        self.make=make        #初始化描述汽车的属性
        self.model=model
        self.year=year
        self.odometer_reading=50
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        # self.odometer_reading=mileage
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("YOU can not roll back an odometer")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

# 上面是父类，下面是子类，创建子类时，父类必须包含在当前文件中，且在子类前面
# 下面是子类，必须在圆括号内指定父类的名称，方法__init__接受创建Car实例所需的信息
# super()是一个特殊函数，让我能够调用父类的方法，该代码让python调用Car类的方法__init__(),让ElectricCar实例中包含这个方法中定义的所有属性，
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)                      # 初始化父类的属性
my_tesla=ElectricCar('tesla',"model s",2019)
print(my_tesla.get_descriptive_name())

# --------------------------------------我是分隔符------------------------------------------------------------------------


# 给子类定义属性和方法
# 让一个类继承另一个类，就可以添加区分子类和父类所需的新属性和新方法了
# 下面来添加一个电动汽车特有的属性，以及一个描述该属性的方法，我们将存储电瓶容量，并编写一个打印电瓶描述的方法
# 本质上就是在类中定义一个self.battery_size=75，这就显示出它的独特性了！，是想创建游戏时，肯定有一些大boss，就是在小boss的基础上加了这一行功能！重要重要！
class Car:
    def __init__(self,make,model,year):
        self.make=make        #初始化描述汽车的属性
        self.model=model
        self.year=year
        self.odometer_reading=50
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        # self.odometer_reading=mileage
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("YOU can not roll back an odometer")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=75
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery")
my_tesla=ElectricCar('tesla',"model s",2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# --------------------------------------我是分隔符------------------------------------------------------------------------

# 将实例用作属性
# 在使用代码模拟实物中，会发现自己给类添加的细节越来越多：属性和方法清单以及文件都越来越长。
# 列如：不断给ElectricCar类添加细节时，我们可能发现其中包含很多专门针对汽车电瓶的属性和方法。--
# --在此情况下，可将这些属性和方法提取出来，放到一个名为Battery的类中，并将一个Battery实例作为ElectricCar类的属性

class Car:
    def __init__(self,make,model,year):
        self.make=make        #初始化描述汽车的属性
        self.model=model
        self.year=year
        self.odometer_reading=50
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        # self.odometer_reading=mileage
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("YOU can not roll back an odometer")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
class Battery:
    def __init__(self,battery_size=75):
        self.battery_size=battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kmh battery")
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
my_tesla=ElectricCar('tesla',"model s",2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

