"""
str()： 函数返回一个用户易读的表达形式
repr()： 产生一个解释器易读的表达形式
字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。  ljust()  center()
"""
for x in range(1,11):
  print(repr(x).rjust(6),repr(x*x).rjust(6),end=" ")
  #注意end的使用
  print(repr(x*x*x).rjust(6))

for x in range(1,11):
  print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

print('{} 网址：{}！'.format('菜鸟教程','www'))

"""
美化表格：
在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
"""
table ={'zhagnsan':1,'lisi':2,'wangwu':3}
for name,number in table.items():
  print('{0:10} ===> {1:10d}'.format(name,number))

"""
旧式字符串格式化，建议使用str.format()
"""
import math
print('常量PI的值近似为：%5.3f' %math.pi)

print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi)) #保留小数后三位