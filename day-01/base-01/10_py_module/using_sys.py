"""
使用python标准库模块的例子：
想使用 Python 源文件，只需在另一个源文件里执行 import 语句
当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。

"""


import sys

print('命令行参数如下：')
for i in sys.argv:
  print("参数：" + i)

print('\n\npython 路径为：', sys.path, '\n')
