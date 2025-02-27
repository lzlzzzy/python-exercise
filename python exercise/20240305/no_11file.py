# 从文件中读取数据
# 读取整个文件
# 要以任何方式使用文件，哪怕仅仅是打印内容，都得先打开文件才能访问它，函数open()括号里是要打开的文件
with open("pi_digits.txt") as file_object:
    contents=file_object.read()
print(contents.rstrip())

# 逐行读取
filename="pi_digits.txt"
with open("pi_digits.txt") as file_object:
    for line in file_object:
        print(line)

# 使用文件的内容
filename="pi_digits.txt"
with open(filename) as file_object:
    lines=file_object.readlines()

pi_string=""                  # 创建一个变量，用来存储圆周率的值
for line in lines:
    pi_string +=line.strip()
print(pi_string)
print(len(pi_string))
a=pi_string*2                 # 这就可以对文件里的东西进行操纵了！
print(a)                      # 读取文件时，要想使用数，就得使用函数int()将其转换为整数或使用float函数

# --------------------------------我是分隔符--------------------------------------------------

# 写入文件,保存数据的最简单的方式之一就是将其写入文件中
# 开始一个空白文件，从零开始
# 调用open时有两个参数open(filenamee,'w')，
# 第一个实参是要打开的文件的名称，第二个实参是以写入模式("w")打开文件，
# 读取模式('r')，写入模式('w')，附加模式('a')，读写模式('r+')
filenamee='programming.txt'
with open(filenamee,'w') as fileobject:
    fileobject.write("I love programming.\n")
    fileobject.write("I love creating new games.\n")

# 附加文件,给文件添加内容，而不是覆盖原有的内容，可以用附件模式打开文件，同理，如果指定的文件不存在，python将为我创建一个文件
filenamee='programming.txt'
with open(filenamee,'a') as fileobject:
    fileobject.write("I also love programming.\n")
    fileobject.write("I also love creating new games.\n")
    fileobject.write("附加厉不厉害，不删除原文件，绝了！\n")

# 存储数据
import json
numbers=[2,3,5,7,11,13]
filenameee='numbers.json'
with open(filenameee,'w') as f:
    json.dump(numbers,f)



