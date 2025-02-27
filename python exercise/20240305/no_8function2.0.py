#使用结合函数和while循环
def get_name(firse,second):
    full_name=f"{firse}{second}"
    return full_name
while True:
    print("\nPlease tell you name")
    f_name=input("first")
    l_name = input("second")
    name=get_name(f_name,l_name)
    print(f"\nHallo,{name}")
#这个循环一直能运行，现在使用break退出运行
    print("\nenter 'q' as end")
    if f_name=="q":
        break
    if f_name=="q":
        break


#传递列表，将列表传递给函数后，函数就能直接访问其内容，下面使用函数来提高处理列表的效率
def greet_users(names):
    for name in names:
        msg=f"Hello, {name.title()}!"
        print(msg)
user_name=["tom","jerry","zzy"]
greet_users(user_name)


#传动任意数量的实参（一个很实用的方法）
#形参中*toppings中的*星号是让python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushroom','green pappers','exter cheese')

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings")
    for topping in toppings:
        print(f"-{topping}")
make_pizza('pepperoni')
make_pizza('mushroom','green pappers','exter cheese')

#结合使用位置实参和任意数量实参，如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后
#你经常会看到通用形参名*args，它也收集任意数量的位置实参
def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green pappers','exter cheese')

#使用任意数量的关键字实参，有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息
#这种情况下，可将函数编写成能够接受任意数量的键值对——调用语句提供了多少就接受多少
#创建用户简历：你知道将收到有关用户的信息，但不确定会是什么样的信息
#形参**user_info中**两个星号的意思是创建一个名为user_info的空字典，并将收到的所有名称值对都放到这个字典中
def build_profile(first,last,**user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
user_profile=build_profile('albert','einstein',
                           location='princeton',
                           field='physics')
print(user_profile)


#将函数存储在模板中，函数的优点之一就是可将代码块与主程序分离，更进一步，将函数存储在称为模块的独立文件中，在导入主程序
#详情见no9pizza和no_9
