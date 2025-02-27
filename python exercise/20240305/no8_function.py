#函数，需要在程序中多次执行同一项任务时，只需调用执行该任务的函数即可
def greet_user():
    #尽量在函数下描述你这个函数的功能，是个好习惯
    print("nh")
    print("使用")          #截至为止是定义函数
print('开始')
greet_user()                #这一行是函数的调用
print('结束')

#把榨汁机看成函数，则榨汁机预制的水果槽是形参，则放入榨汁机的水果是实参（实参是调用函数时传递的数据）
#形参和实参
def greet(discount):
    print(f"商品一律{discount}")
greet("九折")
greet("五折")

def isodd(number):
    if number % 2==1:
        print("奇数")
    else:
        print("偶数")
isodd(25)
isodd(10)


#设置函数返回值，就是把只能在函数内运行的数，放到函数外也可以用
def getArea(lengt):
    area=lengt*lengt
    print(area)
getArea(5)
getArea(15)
if getArea(2)>9:
    print("种西瓜")
#是因为这个if语句输出不了，只能输出函数中的print，输出4，这个情况，我们就要用到返回值了
#返回值return
def getArea(lengt):
    area=lengt*lengt
    return area
result=getArea(5)
print(result)

def getsize(length):
    zhouchang=length*4
    mianji=length*length
    return zhouchang,mianji
print(getsize(8))
print(getsize(6))

#类似于print函数，range函数，append函数，都是python的内置函数，出生下来就可以用

# 匿名函数
square=lambda x:x*x*x     #lambda是匿名函数的关键字，后面的第一个x是形参，后面xxx是要运行的功能
result =square(9)
print((result))

#递归函数，自己运行自己，通常可以算一个数的递加
def sum(n):
    if n<=0:
        return 0
    return n +sum(n-1)    #递归函数的精髓
print(sum(200))

