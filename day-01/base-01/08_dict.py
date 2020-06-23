"""
字典与序列的不同：
序列以连续的整数位索引，字典以关键字为索引。。。。
一对大括号创建一个空的字典：{}
"""
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127  # 添加
print(tel)

print(tel['jack'])  # 查询

print(tel)

del tel['sape']  # 删除
print(tel)

print(list(tel.keys()))  # 转列表

print(sorted(tel.values()))  # 排序

print('jack' in tel)  # 判断是否存在该键

# 构造函数dict() 从键值对元组列表中构建字典
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
# 另一种简便写法
print(dict(sape=4139, guido=4127, jack=4098))

###########字典推导式###########
print({x: x ** 2 for x in (2, 4, 6)})

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
loc_mapping = {val: index for index, val in enumerate(strings)}
print(loc_mapping)


##########返回多个值############
def f():
  a = 5
  b = 6
  c = 7
  return a, b, c  # 实际上返回了一个元组


def f1():
  a = 5
  b = 6
  c = 7
  return {'a': a, 'b': b, 'c': c}  #返回一个字典
