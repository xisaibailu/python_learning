"""
错误：语法错误+异常
"""
#try execept...else 语句
# import sys
#
# for arg in sys.argv[1:]:
#   try:
#     f=open(arg,'r')      #执行代码
#   except IOError:
#     print('cannot open',arg)       #发生异常时执行的代码
#   else:
#     print(arg,'has',len(f.readlines()),'lines')     #没有异常时执行的代码
#     f.close()

def runoob():
  print("hello runoob!")

try:
  runoob()       #执行的语句  try
except AssertionError as error:   #发生异常时执行的语句 execept
  print(error)
else:           #没有异常时执行的代码 else
  try:
    with open('../tmp/foo.txt') as file:    #预定义的清理 with
      read_data = file.read()
  except FileNotFoundError as fnf_error:
    print(fnf_error)
finally:        #不管有没有异常都会执行的代码  finally
  print('good!')

