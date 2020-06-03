"""
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

数据类型：
Python3 的六个标准数据类型中：
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

"""

# number：int,float,bool,complex(复数)
a, b, c, d = 1, 2, 3, "多变量赋值"
print(a, b, c, d)

# bool：true->1,false->0

# 列表 List
arrList = ['abc', 785, 2.24, 'runoob', 70.2]
# 查询
list1 = ['matai', 'make', 'lujia', 1994]
list2 = [1, 2, 3, 4, 5, 6]
print("list1[0]", list1[0])
print("list2[1:5]", list2[1:5])

# update list
list1[3] = 2000
print("更新后的第三个元素", list1[3])

# delete list element
del list1[3]
print("删除list1[3]后的list为", list1)

# 其它操作
print("长度", len(list1))
print("组合", list1 + list2)
print("重复", ['hi'] * 4)
print("元素是否存在", 3 in [1, 2, 3])
for x in [1, 2, 3]:
  print("迭代", x)
print("---------------------------------------------")
# 元组 tuple
# 注意：当元组中只包含一个元素时，需要在元素后面添加逗号
tup1 = ('matai', 'make', 'lujia', 'yuehan', 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = 'a', 'b', 'c', 'd', 'e'
print("类型", type(tup3))
tup4 = (10,)
print("要加号,类型才能显示为元组", type(tup4))

# 元组的操作与list基本类似

# 字典
dict = {"name": "runoob", "age": 7, "class": "first"}
dict["age"] = 8  # 更新
dict['school'] = "菜鸟"  # 添加
del dict['name']  # 删除
dict.clear()  # 清空字典
del dict  # 删除字典
