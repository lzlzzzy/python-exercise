#将函数存储在模板中，函数的优点之一就是可将代码块与主程序分离，更进一步，将函数存储在称为模块的独立文件中，在导入主程序


def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings")
    for topping in toppings:
        print(f"-{topping}")
        