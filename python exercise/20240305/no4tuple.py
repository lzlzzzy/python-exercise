#列表非常适合存储在程序运行期间可能改变的数据集，列表是可修改的，这对处理游戏中的角色列表至关重要，详情请见no3
#然而，你也需要创建一些不可被修改的元素，列如boss的血量，树木的高度等等等，则python将这种不可变的列表称为元组（实际上就是列表）
#元组本质是就是列表，书写的区别在于元组使用圆括号而不是中括号，定义完元组后，就可以使用索引来访问其元素（和访问列表一样）
#准确来说，元组是由逗号标识的，列如a=(12,)这个才是元组，和a=(12)这个差别很大，若要定义一个元组，必须在里面的元素后加上逗号
#这章就介绍一下元组，一般用不上

dimension=(200,90)
print(dimension[0])
print(dimension[1])
#遍历元组中的值
for dimemn in dimension:
    print(dimemn)

#修改元组里的值，直接重新定义一个
dimension=(200,90)
dimension=(890,1290)