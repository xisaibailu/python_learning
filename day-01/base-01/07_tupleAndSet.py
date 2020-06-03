"""
元组由若干逗号分隔的值而成
注意：元组在输出时总是有括号的，输入时可能有或没有括号
"""
t = 1234, 4321, 'hello'
print(type(t))
print(t)  # (1234, 4321, 'hello')
u = t, (1, 2, 3, 4)
print(u)

"""
集合set
集合是一个无序不重复元素的集
基本功能：关系测试、消除重复元素
注意：可以用（{}）创建集合，但是如果创建一个空集合，必须使用set() 而不是{}，后者创建的是一个空字典
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(type(basket))
print(basket)  # 删除重复
print(' orange '.strip() in basket)  # 检测成员

###############两个集合的操作###############
a = set('abcdefgh')
b = set('alacazam')
print(a)  # a中唯一的字母
print(a - b)  # 在a中的字母，但不在b中
print(a | b)  # 在a或b中的字母
print(a & b)  # 在a和b中的字母
print(a ^ b)  # 在a或b中的字母，但不同时在a和b中

# 集合也支持推导式
c = {x for x in a if x not in 'abc'}
print(c)
