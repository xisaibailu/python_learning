#第一个代码
import keyword
print(keyword.kwlist)

print("============================")

#单行注释
'''
多行注释1
多行注释2
'''

"""
多行注释
"""
print("Hello python!") #第二个注释

#行与缩进
if True:
  print("True")
else:
  print("false")

#多行语句 使用"\"
total = "item_one_" + \
        "item_two_" + \
        "item+three"
print(total)

"""
模块导入
1.将整个模块(somemodule)导入，格式为： import somemodule
2.从某个模块中导入某个函数,格式为： from somemodule import somefunction
"""