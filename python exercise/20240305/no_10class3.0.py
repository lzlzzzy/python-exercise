class Car:
    def __init__(self,make,model,year):
        self.make=make        #初始化描述汽车的属性
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

my_new_car=Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#出售里程表是0的汽车不多，使用要一种方式来修改属性的值
#直接通过实例直接访问它，使用句号表示法直接访问并设置汽车的属性odometer_reading
my_new_car.odometer_reading=23
my_new_car.read_odometer()

#--------------------------------------我是分隔符------------------------------------------------------------------------

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
# --------------------------------------用方法init来替我更新属性----------------------------------------------------
    # -----------还可以更高端一点，对方法update_odometer进行扩展，使其在修改里程表读数时做些额外的工作---------------
    def update_odometer(self,mileage):
        # self.odometer_reading=mileage
    #将里程表读数设置为指定的值，禁止将里程表读数往回调
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("YOU can not roll back an odometer")
#通过方法对属性的值进行递增，有时候需要将属性值递增特定的量，而不是将其设置为全新的值
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

my_new_car=Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(45)
my_new_car.read_odometer()

my_used_car=Car('subaru','outback',2015)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)              #通过方法对属性的值进行递增，有时候需要将属性值递增特定的量，而不是将其设置为全新的值
my_used_car.read_odometer()


