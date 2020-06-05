# """
# print("你好!")  # 字符串
# print(2333)
# print(2.333)
# print(True)
# print(a()) #元组
# print(a[]) #数组


# """

a = str(input("请输入："))
b = str(input("请输入："))

# print("两端字符串的长度是：",len(a)+len(b))

#元组，下标，从0开始编号且不重复
#index()查找某个值的编号
#count()统计某个值的编号

a = (1,2,3,4,"合合","hehe","呵呵","合合","嘻嘻",2.03,True,False)

print(a[5])
print(a.index("合合"))
print(a.count("合合"))

b = (a,"hehe","圈圈")
print(b[0][6])

#切片
print(a[0:5]) #左闭右开
print(a[:4]) #从最开始到4
print(a[7:]) #从7到最后


a = [1,2,3,4,"合合","hehe","嘻嘻",2.03,True,False]
a.append("append1")   #往数组中追加数据
a.append("append2")  
print(a)
# # 区别：元组写好不可修改，数组写好后可以进行修改

a. insert(4,"在位置4插入一个值")
print(a)
b = a.pop(0) #剪切
c = a.pop(0)
print(b+c)
print(b)
print(c)

# a.clear()  #清空数组
# print(a)

xx = ["你好","再见"]
a.extend(xx)
print(a+xx)  #数组之间可以相加

print(a)
a.remove("嘻嘻")
print(a)

"""
python的语法
所有的方法都是小括号结尾。比如，print(),input(),len()
元组、数组、字典的取值，都是用中括号，比如a[0]
元组、数组、字典的定义，分别是(),[],{}
"""

"""
字典的特点
1. 字典中的值没有顺序
2、字典的结构必须是 键值对的结构。key:value
"""

# a = {
#     "name":"张三",
#     0:"哈哈",
#     "age":23,
#     }
# # 取值
# print(a["name"])
# # 新增
# a["height"] = "183cm"
# print(a)
# # 修改
# a["name"] = "李四"
# print(a)

# b = a.get("name")
# print(b)
# b = a.pop("name")
# print(b)
# print(a)

# a.update(name=1111)
# print(a)


# # 数组和字典的删除

# del a["name"]
# print(a)


"""
联系：获取用户输入的个人信息，并且存储到字典中。
个人信息包括了，name,age,sex.
"""

# 写法一
name = str(input("请输入姓名："))
age = int(input("请输入年龄："))
sex = str(input("请输入性别："))
a = {"name":name,"age":age,"sex":sex}
print(a)

#写法二
name = str(input("请输入姓名："))
age = int(input("请输入年龄："))
sex = str(input("请输入性别："))
userinfo = {}
userinfo.update(name=name,age=age,sex=sex)
print(userinfo)






