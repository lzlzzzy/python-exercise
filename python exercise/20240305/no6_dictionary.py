#字典：键值对！键不可相同，若相同，则值会进行覆盖
#空字典的使用
# zzy={}
# zzy['tall']=180
# zzy["color"]='yellow'

zzy={'tall':180,'color':'yellow',18:'i'}
print(zzy['tall'])
print(zzy[18])
#添加键值对
zzy["x_position"]=0
zzy["y_position"]=25
print(zzy)

#修改字典里的值,和添加键值对很类似
zhang={'color_zhang':'green'}
zhang['color_zhang']='yellow'
print(f"The zhang is now {zhang['color_zhang']}")

#实践操作：修改键值对的值
#下面介绍一个小例子理解（游戏里boss）
alien_0={"x_where":0,'y_where':25,'speed':55}
print(f"Ori_where:{alien_0['x_where']}")
#根据速度看外星人的x位移
if alien_0['speed']<=10:
    x_increase=1             #前进1格
elif alien_0['speed']>=11 and alien_0['speed']<=30:
    x_increase=2
else:
    x_increase=3
alien_0['x_where']=alien_0['x_where']+x_increase    #注意这里加了一项
print(f"NEW_where:{alien_0['x_where']}")

#删除键值对：del语句,且删除的键值对会永远消失
zhen={'color':'green','point':5}
print(zhen)
del zhen['point']
print(zhen)

#键值对太多,不用一直写在一行里
love_language={
    'zhang':"c",
    'zhen':'python',
    'yang':'ruby'
}
print(love_language)

#使用get()来访问值，优点在于如果这个键不存在计算机也不会报错，反而会返回一个默认值
#使用print(alinen_0['color'])这个功能也可以获得值，但是如果这个键不存在就会麻烦
#get("1","2")使用get，这个1用于get字典里的键，这个2是当这个键不存在时可输出这个2
alien_0={'color':'red','speed':25}
print_value=alien_0.get('point')
print(print_value)
print_val=alien_0.get('热点',"没有这个哦，宝宝")
print(print_val)

#遍历字典:键值对:items，键:keys，值:values.
#遍历所有键值对items
user_0={'usename':'zzy','first':'z','last':'zy',}
for hhh,value in user_0.items():
    # print({key})
    # print({value})    更美观一点
    print(f"\nthis:{hhh}")
    print(f"that:{value}")

#遍历字典中的所有键keys
love_language={'zhang':"c",'zhen':'python','yang':'ruby','zzy':'chinese'}
for name in love_language.keys():
    print(name.title())

#遍历字典中的所有值values
love_language={
    'zhang':"c",
    'zhen':'python',
    'yang':'ruby',
    'zzy':'chinese'
}
for language in love_language.values():
    print(language.title())

#嵌套：有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这就是嵌套
#当我要的字典不止1个或者很多，比如我要30个外星人（小杂兵），每个外星人都有颜色点数速度等，这时肯定需要字典，但你能敲30个字典吗
#嵌套：将一系列字典存储在列表中
aliens=[]
#创建30个小兵
for alien_number in range(30):
    new_alien={'color':'red','point':10,'speed':25}
    aliens.append(new_alien)
# #看看前五个小兵
# for alien in aliens[:5]:
#     print(alien)
#随着时间的进行，这个外星人小兵会变色并且速度加快，点数增加，那怎么去修改他们呢？
#修改前三个外星人,以外星人颜色参考，若外星人是红的，它就进化
for alien in aliens[:3]:
    if alien["color"]=="red":
        alien['color']="yellow"
        alien["point"]=50
        alien['speed']=60
#看看前五个小兵
for alien in aliens[:5]:
    print(alien)

#嵌套：将列表作为值存储在字典中
pizza={
    'crust':'thick',
    'tops':['mushrooms','extra cheese']
}
for top in pizza['tops']:
    print(top)

#在字典中嵌套字典，列如：将用户名作为键，然后将用户的信息（姓，名，居住地）放到一个字典中
users={
    'xiaoiming':{
        'first':'zhang',
        'last':'xiaoming',
        "location":'funan',
    },
    "dahong":{
        'first':'zhang',
        'last':'dahong',
        "location":'fuyang',
    },
}
for username,user_info in users.items():
    print(f'\nUsername:{username}')
    full_name=f"{user_info['first']}{user_info['last']}"
    location=user_info["location"]
    print(f"Full_name:{full_name}")
    print(f"lacation:{location}")