# 导入类
# 为简洁，python可允许类存储在模块中，然后在主程序中导入所需的模板
# 导入多个类
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
    def get_range(self):
        if self.battery_size==75:
            range=260
        elif self.battery_size==100:
            range=315
        print(f"This car can go about {range} miles on a full charge")

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()