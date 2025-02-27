#从一个模板中导入多个类
from no_10classll import Car,ElectricCar
my_beetle=Car('volkswagen','beetle',2019)
print(my_beetle.get_descriptive_name())
my_tesla=ElectricCar('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())