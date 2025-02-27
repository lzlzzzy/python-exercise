# 导入了多个类使用
from no_10classll import ElectricCar
my_tesla=ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

