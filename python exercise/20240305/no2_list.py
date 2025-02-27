# 列表，提取元素
bic=["abc","abicas","ajis","axsiox"]
print(bic)
# 列表的第一个元素是从0开始
print(bic[3])
print(bic[3].title())
message=f"my first was a {bic[0].title()}"
print(message)
# 修改列表的元素
bic[0]="adsd"
print(bic)
#增加列表的元素append
bic.append("zhangzhenyang")
print(bic)

#增加列表里的元素
abc=[]
abc.append(1)
abc.append(32)
abc.append(900)
print(abc)
#增加列表中的元素，插入！insert,前者是位置，后面是元素
abc.insert(0,"zjoajoq")
print(abc)
# 从列表中删除元素del,后面跟上列表要删除的位置
del abc[2]
print(abc)

# 使用pop弹出（删除）元素.pop后的括号可带上列表位置的树，不带数就默认为弹出最后一个数
# 别忘了，每当我使用pop后，弹出的元素就不在该列表中了
mot=["hon",12,"suz","koqdm"]
popmot=mot.pop()
print(mot)
print(popmot)
print(f"The last mostau I own was a {popmot.title()}")

# 使用remove移走元素,你要特指这个元素，也就是你提前就要想好你要移除的元素是叫什么
list = [1, 2, 3, 4, 5]
list.remove(1)
print (list)

# 组织列表，让列表里的元素按照某个特定的顺序来呈现信息
# sort是永久性的改变元素排列顺序，且sort按照字母来排序，规定：字母一定要小写
cars=["qm","xn","zmkla","msknq"]
cars.sort()
print(cars)

#sorted可保留元素原来的排列顺序，同时以特定的顺序来呈现他们。sorted是一个函数，临时改变直接用！
car=["abuix","pioqsm","zioqm","maxm"]
print("here is the original list:")
print(car)
print("\nhere is the sorted list:")
print(sorted(car))
print("\nhere is the original list again:")
print(car)

#按照相反顺序打印元素reverse()
sabicu=[12,1892,1021228]
sabicu.reverse()
print(sabicu)

#len()可快速获知列表的长度
zzy=["nquid","q","xqs","sqcs"]
print(len(zzy))