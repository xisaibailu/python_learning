# 斐波那契数列
# 两个元素的综合确定了下一个数
# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a + b

########### end关键字：############
# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
# a, b = 0, 1
# while b < 1000:
#     print(b, end=',')
#     a, b = b, a + b

############## 数字猜谜游戏###############
# number = 7
# guess = -1
# print("游戏开始")
# while guess != number:
#     guess = int(input("请输入你猜的数字"))
#
#     if guess == number:
#         print("恭喜你，猜对了！")
#     elif guess < number:
#         print("猜小了")
#     elif guess > number:
#         print("猜大了")

############ while语句###############
# count = 0
# while count < 5:
#     print(count, "小于5")
#     count = count + 1
# else:
#     print(count, "大于或等于5")

# while True:
#     print('hello python')

############## for 语句##############
# sites=['java','sql','js','python']
# for site in sites:
#     if site=="python":
#         print("python")
#         break
#     print("循环数据",site)
# else:
#     print("没有循环数据")
# print("完成循环！")

################ range()函数###############
# for i in range(0,20,3):
#     print(i)
print(str(list(range(4))))
print(str(list(range(1, 4))))

# 结合range()和list()遍历一个序列
# list_arr = ['java', 'sql', 'js', 'python']
# for i in range(len(list_arr)):
#     print(i, list_arr[i])

# 输出质数
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, '等于', x, '*', n // x)
#             break
#     else:
#         # 循环中没有找到元素
#         print(n, '是质数')

############ 迭代器###############
import sys  # 引入sys 模块

list1 = range(1, 5)
it = iter(list1)  # 创建迭代器对象

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

