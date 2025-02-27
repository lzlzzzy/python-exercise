#用户输入和while循环
#input使用

# message=input("")
# print(message)
message=input("you can input something:")
print(message)
name=input('please tell you name: ')
print(f"are you sure you use this name{name}")

#使用函数input时，python将用户输入解读为字符串，为解决可以获取数值的问题，可使用函数int
height=input('how tall you are: ')
height=int(height)
if height<=18:
    print("\n NO you are not allow to play this game")
else:
    print("you can play it")

#求模运算符：两个数相除并返回余数
#4%3=1，5%3=2，6%3=0，7%3=1
#如果一个数可被另一个数整除，余数就为0，因此求模运算将返回0，可利用这个来判断一个数为奇数还是偶数
number=input("give me a nub i will tell you if it is even or odd: ")
number=int(number)
if number %2 ==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

#while循环，for循环用于针对集合中的每个元素都执行一个代码块，而while循环则不断运行，直到指定的条件不满足为止
#很多游戏就包含while循环，确保玩家想玩游戏时不断运行，并在玩家想退出时停止运行
num=1
while num <=5:
    print(num)
    num+=1

#让用户选择何时退出，在下例，我们定义了一个 退出值 只要用户输入达到不是这个值，程序就接着运行
#很明显，当这个程序只有我主动打quit才能结束循环，不然循环一直运行下去
#低配版
# message=""
# while message !='quit':
#     message =input("")
#     print(message)
prompt="\nGive me a word,and i will repeat it"
prompt+="\nEnter 'quit' to end this circle"
message=""
while message !='quit':
    message =input(prompt)
    print(message)

#使用标志,看看和上面一个有上面不一样，发现，上面一个局限性太大，一般不会只有一个message，可能message不等于a，mess不等于b等等等等，用这个标志
#这个标志，可充当程序的交通信号灯，只有两个条件，标志为true运行，标志为false不运行
prompt="\nGive me a word,and i will repeat it"
prompt+="\nEnter 'quit' to end this circle"
active =True
while active:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)

# 使用break退出循环（在任何python中的循环都可以用break来结束，列如，可以用break退出while循环，退出遍历列表，或退出字典的for循环）
#该下循环，问你想要去哪个城市，没有标志答案，程序肯定要一直运行下去，这个时候i，就要用break来打破循环！
prompt="\nwhat is the city you want"
prompt+="\nEnter 'quit' to end this circle"
while True:                                      #很明显，这个玩意是true，肯定会一直运行下去
    city=input(prompt)
    if city=='quit':
        break
    else:
        print(f"i want to this city {city}")

#使用continue：要返回循环开头，并根据条件测试结果决定是否继续执行循环
current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number)
#continue会持续运行循环，只为看是否符合while循环条件
current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        break
    print(current_number)

#当你用while不小心打出了无限循环，列如：x=1;while<5;print(x);因为while就是定值，就是小于5，那这个程序会无限的打印x
#无限循环时可按ctrl+c,也可关闭显示程序输出的终端窗口

#使用while来循环处理列表和字典
#在列表之间移动元素
