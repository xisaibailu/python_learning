#第一种导入方式（推荐使用这种方式）
# import fibo
#
# fibo.fib(1000)
#
# s = fibo.fib02(100)
# print(s)

#第二种导入方式 (不推荐使用)
# from fibo import fib,fib02
# fib(1000)
# a = fib02(100)
# print(a)

#测试内置的函数dir(), 其可以找到模块内定义的所有名称
import fibo,sys
print(dir(fibo))
print(dir(sys))