#if语句
#双等号==，检验左右两边是否相等，相同就ture，不相同就false，且在python中检查是否相等时区分大小写，列如：zzy和Zzy不相同，为false
cars=['audi','bmw','sub','toty']
#for car in cars:引出一个语法：for car not in cars:,自己体会吧
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

#不相等：！=，其中！感叹号表示”不“，
a=5
if a!=1:
    print("hhh")

#数值比较，<=,>=,==,!=
#检查多个条件，and,or,
a1=22
a2=18
if a1>=21 or a2>=21:
    print("hhh")
if a1>=21 and a2>=21:
    print("hhha")
else:
    print("hhhh")

#if-else语句   if-elif-else语句,但要注意：else是一个包罗万象的语句，可能会识别恶意的数据，所以可以换成最后一个用elif来控制剩下的区间
age=19
if age <4:
    print("you shoule pay 0")
elif age<18:
    print("you shhuold pay 25")
elif age < 65:
    print("you shuold pay 45")
else:
    print("you shuold pay 70")

#使用列表处理数据
foods=["egg","apple","banann","water"]
#但是店突然这时候里面没有egg了，怎么办
for food in foods :
    if food =="egg":
        print("很抱歉，鸡蛋没了")
    else:
        print(f"但有{food}")

#使用多个列表
foods=["egg","apple","banann","water"]
needs=["egg","water","boss"]
for need in needs:
    if need in foods:
        print(f"我们有这个{need}")
    else:
        print(f"我们没有这个{need}")
print("都给你了 ")

