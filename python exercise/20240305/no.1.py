# pycharm中很重要的快捷键
# ctrl+/      注释
# shift+enter 下一个行
# ctrl+f 查询
# 光标初始,shift最后,全选


#字符串，单引号双引号

#变量
message='she said:"i will back"'
print(message)

#字符串输入大写
message='she said:"i will back"'
print(message.title())
print(message.lower())
print(message.upper())
#这种字符串名为f字符串，f是format的缩写,   \t是前面给空格，美观  \n是换行
fir="zhang"
sec="zhenyang"
al=f"{fir}  {sec}"
print(al)
print(f"\tHello,\n\ti said{al.title()}!")

#test
a="zhangzhenyang"
print(f"hello,{a},would you please help me?")



