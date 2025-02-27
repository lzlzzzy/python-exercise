#在no2中，学习了怎么创建简短的列表，现在，你将学习如何遍历整个列表（一般for循环读取）
#循环让你能够对列表的每个元素都采取一个或一系列相同的措施，从而高效的处理任何长度的列表
#列如，在游戏里，每个元素都是一个角色，可以使用这个for循环，遍历所有角色，在最后加一个游戏开始按钮
cats=["tom","june","jerry","july"]
for cat in cats:
    print(cat)
    print(f"{cat.title()},that was a good animals")
print("Game coming")

#数值列表range函数
for a in range(1,5):
    print(a)

#要创建数值列表，可用list（）将range（）的结果直接转化为列表
num=list(range(1,6))
print(num)
#再来一个
num1=list(range(1,11,3))
print(num1)

#想要对一个数值列表中的数做变化，要先利用for循环取出该数，可定义一个sum等于该列表的数，后在创造一个你想要的变量，对该列表里的数进行操作
a=[1,2,3,3]
for sumss in a:
    b=sumss**2
    print(b)

sa=[]
for sums in range(1,11):
    a=sums**2
    sa.append(a)
print(sa)
#对数字列表执行简单的运算，min，max，sum
print(sum(sa))
print(max(sa))
print(min(sa))

#如何使用列表的一部分，python称为切片
zzy=[19,128,3278,1]
print(zzy[-3:-1])

#在no3最上面你学习了怎么遍历整个列表，现在，你将学习如何遍历部分列表（遍历切片）,很明显，就取的dogs，cats后面加上它的切片
#在编写游戏时，所有玩家的得分是一个列表，但是，为了体现竞技性，对所有列表进行切片遍历，只取前三名的成绩，公布
dogs=["char","adjust","appoint","dispoint","respect"]
print("here is the first three playor on my team:")
for dog in dogs[0:3]:
    print(dog.title())

#你和你姐姐都喜欢从水果，你喜欢四种，刚好你姐姐也喜欢这四种，这时我们就要复制列表了
zzyz=["apple","banann","origan","water"]
zc=zzyz[:]
print(zzyz)
print(zc)
#这个时候，突然你又喜欢吃鸡蛋了，而你姐姐却喜欢从青菜了
zzyz.append("egg")
zc.append("cai")
print(zzyz)
print(zc)

#列表非常适合存储在程序运行期间可能改变的数据集，列表是可修改的，这对处理游戏中的角色列表至关重要
#然而，你也需要创建一些不可被修改的元素，列如boss的血量，树木的高度等等等，则python将这种不可变的列表称为元组（实际上就是列表），详情请见no4

