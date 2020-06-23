"""
列表：list
insert（i，x）
remove（x）
sort（）
count（）
append（x）
reverse（）
index（x） 返回列表中第一个值为x的索引，如果没有匹配到返回一个错误
"""
# a=[66.25,333,333,1,1234.5]
# print(a.count(333),a.count(66.25),a.count("x"))
# a.insert(2,-1)
# a.append(333)
# print(a)
#
# print(a.index(333))
# a.remove(333)
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)

"""
将列表作为堆栈使用：append（），pop（）
"""
# stack=[3,4,5]
# stack.append(6)
# print(stack)
#
# print(stack.pop())
# print(stack)

"""
将列表当作队列使用
"""
# from collections import deque
#
# queue = deque(["John", "make", "dawei"])
# queue.append("Terry")
# queue.append("Graham")
# queue.popleft()
# queue.popleft()
# print(queue)

"""
列表推导
"""
# vec = [2, 4, 6]
# print([[x, x ** 2] for x in vec])
#
# vec1 = [2, 4, 6]
# vec2 = [4, 3, -9]
# print([x * y for x in vec1 for y in vec2])
# print([x + y for x in vec1 for y in vec2])
# print([vec1[i] * vec2[i] for i in range(len(vec1))])

"""
嵌套列表解析
将3X4 的矩阵列表 转为4X3 的列表
"""
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]
#第一种方法
for i in range(4):
    print("值为：",[row[i] for row in matrix])
print([row[1] for row in matrix])
print([[row[i] for row in matrix]for i in range(4)])

#第二种方法
# transposed=[]
# for i in range(4):
#   transposed.append([row[i] for row in matrix])
#
# print(transposed)

"""
del 语句
可以从一个列表依索引而不是值来删除一个元素
"""
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)


