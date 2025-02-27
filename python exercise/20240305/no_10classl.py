# 导入类
# 为简洁，python可允许类存储在模块中，然后在主程序中导入所需的模板
# 导入单个类
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
