# python_learning Notes

### day-01
1. 基础：注释、缩进、模块导入
2. 数据类型：Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
    * 不可变数据：Number(数字)、String(字符串)、Tuple(元组)
        *Number: int、float、bool、complex（复数）
         ```
         a, b, c, d = 20, 5.5, True, 4+3j
         print(type(a), type(b), type(c), type(d))
         >>> <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
          注：bool类型：0表示False，1表示True
             数值的除法包含两个运算符： / 返回一个浮点数
                                  // 返回一个整数
         ```
    * 可变数据：List(列表)、Dictionary(字典)、Set(集合)
* 多变量赋值
  ```
  a,b,c,d =1,2,3,"多变量赋值"
  ```
 
* 列表List的常用操作：
  ```
  新建：list = ['abc', 785, 2.24, 'runoob', 70.2]
  根据下标查询： list[0] 或 list2[1:5])
  更新： list[3] = 2000
  删除： del list[3]
  其它操作：
    print("长度", len(list1))
    print("组合", list1 + list2)
    print("重复", ['hi'] * 4)
    print("元素是否存在", 3 in [1, 2, 3])
    for x in [1, 2, 3]:
      print("迭代", x)
  ```
* 元组 tuple
> 注意：
>  当元组中只包含一个元素时，需要在元素后面添加逗号
>  元组不可修改
  ```
  tup1 = ('matai', 'make', 'lujia', 'yuehan', 2000)
  tup2 = (1, 2, 3, 4, 5)
  tup3 = 'a', 'b', 'c', 'd', 'e'
  print("类型", type(tup3))
  tup4 = (10,)
  print("要加号,类型才能显示为元组", type(tup4))

  元组操作与list基本类似  
  ```    
* 字典 dict
  ```
  dict = {"name": "runoob", "age": 7, "class": "first"}
  dict["age"] = 8  # 更新
  dict['school'] = "菜鸟"  # 添加
  del dict['name']  # 删除o
  dict.clear()  # 清空字典
  del dict  # 删除字典
  ```       
* 字符串 String
  > 包含字符串的截取、多行字符串的使用，新的格式化字符串语法：f-string
  ```
    str='Runoob'

    print(str)
    print(str[0:-1])
    print(str[0])
    print(str[2:5])
    print(str[2:])
    print(str*2)
    print('----------------------------------')
    print('hello\nrunoob')
    print(r'hello\nrunoob')
    
    #三引号
    para_str="""
    这是一个多行字符串实例，多行字符串可以使用制表符
    tab(\t)
    也可以使用换行符[\n]
    """
    print(para_str)
    
    #f-string
    name = "xsbl"
    str1 = f'{name} shuai'
    print(str1)
  ```
* 复合赋值
```
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

代码 a, b = b, a+b 的计算方式为先计算右边表达式，然后同时赋值给左边，
右边表达式的执行顺序是从左往右的，等价于：
    n=b
    m=a+b
    a=n
    b=m

``` 
  
* end 关键字
> 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符

* if语句
> if -- elif -- else

* while语句
> python 中没有do...while循环
```
while 循环使用else语句:

count = 0
while count < 5:
    print(count, "小于5")
    count = count + 1
else:
    print(count, "大于或等于5")
```

* for语句
```
#!/usr/bin/python3
 
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
```

* range() 函数
> range(5)   #0,1,2,3,4
> range(5,9)  #5,6,7,8
> range(0,10,3) # 0,3,6,9  3为步长
> 使用list转为列表： list(range(5))
```
结合range()和list() 遍历一个数字序列
 list_arr = ['java', 'sql', 'js', 'python']
 for i in range(len(list_arr)):
   print(i, list_arr[i])
```

* 函数
```
def print_welcome(name): 
    print(name,"is beautiful")
调用：print_welcome("Carrie")
```

* 参数传递
> 在 python 中，类型属于对象，变量是没有类型的：
a=[1,2,3]
a="Runoob"
以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，
她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。

>参考：https://www.runoob.com/python3/python3-function.html

### 可更改（mutable）与不可更改（immutable）对象
> 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

> 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
>
>python 函数的参数传递：
>
>不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。
>          比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
>
>可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

>python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

* python传不可变对象
```
#!/usr/bin/python3
 
def ChangeInt( a ):
    a = 10
 
b = 2
ChangeInt(b)
print( b ) # 结果是 2
```
    实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，
    a 和 b 都指向了同一个 Int 对象，在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它。

* 传可变对象
>可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：
```
#!/usr/bin/python3
 
# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)
```
    传入函数的和在末尾添加新内容的对象用的是同一个引用。故输出结果如下：

    函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
    函数外取值:  [10, 20, 30, [1, 2, 3, 4]]

### 不定长参数
    * 定义：你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，
           声明时不会命名
    * 第一种，以一个“*”的方式：加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
    ```
    定义：def printinfo(arg1,*vartuple):
            函数体
    调用：printinfo(1,60,70) 
    输出：1, (60,70)
    ```
    * 第二种，以两个“**”的方式：加了两个星号 ** 的参数会以字典的形式导入
    ```
    定义：def printinfo(arg1,**vardict):
            函数体
    调用：printinfo(1,a=3,c=3) 
    输出：1, {'a'=3,'c=3'}
    ```
    > 补充: 调用函数时可使用的正式参数类型：必需参数、关键字参数、默认参数、不定长参数
    
* 匿名函数
> 使用lambda创建匿名函数，所谓匿名，意即不再使用def语句这样标准的形式定义一个函数。
>
>   1.lambda只是一个表达式，函数体比def简单很多。
>
>   2.lambda的主体是一个表达式，而不是代码块，仅仅能在lambda表达式中封装有限的逻辑进去
>
>   3.lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
>
>   4.虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
```
# 使用lambda创建匿名函数
sum1 = lambda arg1, arg2: arg1 + arg2
# 调用
print("相加后的指", sum1(10, 20))  #结果为30
```

* return语句

    注：不带参数值的return语句返回None
    
### python数据结构

* 列表：
    * 将列表作为堆栈使用：append（），pop（） 【后进先出】
    * 将列表当作队列使用：效率不高【先进先出】 
    ```
    from collections import deque

    queue = deque(["John", "make", "dawei"])
    queue.append("Terry")
    queue.append("Graham")
    queue.popleft()
    queue.popleft()
    print(queue)

    ```

### 列表推导式
   
   提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，
   用其获得的结果违生成新列表的元素，或者根据确定的判定条件创建子序列
   每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。
   如果希望表达式推导出一个元组，就必须使用括号。

```
>>> vec1 = [2, 4, 6]
>>> vec2 = [4, 3, -9]
>>> [x*y for x in vec1 for y in vec2]
[8, 6, -18, 16, 12, -36, 24, 18, -54]
>>> [x+y for x in vec1 for y in vec2]
[6, 5, -7, 8, 7, -5, 10, 9, -3]
>>> [vec1[i]*vec2[i] for i in range(len(vec1))]
[8, 12, -54]

列表推导式可以使用复杂表达式或嵌套函数：

>>> [str(round(355/113, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

* 嵌套列表解析

将4X3的矩阵列表转为4X3的列表:
```
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]

#第一种方法
print([[row[i] for row in matrix]for i in range(4)])
等同于：
for i in range(4):
    print("值为：",[row[i] for row in matrix])

#第二种方法
# transposed=[]
# for i in range(4):
#   transposed.append([row[i] for row in matrix])
#
# print(transposed)
```

* del语句

可以从一个列表依索引而不是值来删除一个元素
```
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)
```

* 元组和序列
> 元组由若干逗号分隔的值而成
>
>注意：元组在输出时总是有括号的，输入时可能有或没有括号
```
t = 1234, 4321, 'hello'
print(type(t))
print(t)  # (1234, 4321, 'hello')
u = t, (1, 2, 3, 4)
print(u)
```

>集合是一个无序不重复元素的集
基本功能：关系测试、消除重复元素
注意：可以用（{}）创建集合，但是如果创建一个空集合，
>必须使用set() 而不是{}，后者创建的是一个空字典
```
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

```

### 字典
1. 序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
2. 理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
3. 一对大括号创建一个空的字典：{}。
```
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
```

### 遍历技巧
遍历技巧：
1. item（）,遍历字典中的键和值
2. enumerate（），遍历序列中的索引和对应的值
3. zip()，遍历两个或更多的序列
4. reversed()，反向遍历一个序列
5. sorted（），按顺序遍历一个序列






### python分析excel数据
参考:https://blog.csdn.net/u012063773/article/details/73846343?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase

