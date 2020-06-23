# 定义一个函数
def area(width, length):
  print("area", width * length)


def print_welcome(name):
  print(name, "is beautiful")


# 函数调用
# print_welcome("Carrie")
# area(3, 4)

################参数传递#####################
'''
在 python 中，类型属于对象，变量是没有类型的：
a=[1,2,3]
a="Runoob"
以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，
她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。

参考：https://www.runoob.com/python3/python3-function.html
'''


# 1. python传不可变对象实例
def ChangeInt(a):
  a = 10
  print(a)  # 10
  print(b)  # 2
  return

b = 2
ChangeInt(b)
print("b=",b)  # 结果为2


############不定长参数###################
# 单个*
def printInfo(arg1, *vartuple):
  print("输出")
  print(arg1)
  print(vartuple)


# 调用printInfo
printInfo(40, 5, 60, 70)


# 两个**
def printInfo_1(arg1, **vardict):
  print("输出")
  print(arg1)
  print(vardict)


# 调用
printInfo_1(1, a=2, b=3, c=4)

#############匿名函数##############
# 使用lambda创建匿名函数
sum1 = lambda arg1, arg2: arg1 + arg2
# 调用
print("相加后的指", sum1(10, 20))
