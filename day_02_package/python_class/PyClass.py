############类的对象############
# class PyClass:
#   i=12345
#   def f(self):
#     return "hello world"
#
# #实例化类
# x=PyClass()
#
# #访问类的属性和方法
# print("访问属性",x.i)
# print("访问方法：",x.f())

############单继承################
# 类定义
class people:
  # 定义基本属性
  name = ''
  age = 0
  # 定义私有属性
  __weight = 0

  # 定义构造方法
  def __init__(self, n, a, w):
    self.name = n
    self.age = a
    self.__weight = w

  def speak(self):
    print('{} 说：我{}岁。'.format(self.name, self.age))


# 单继承示例
class student(people):
  grade = ''

  def __init__(self, n, a, w, g):
    # 调用父类的构函
    people.__init__(self, n, a, w)
    self.grade = g

  # 覆写父类的方法
  def speak(self):
    print('{} 说：我{}岁了，我读{}年级。'.format(self.name, self.age, self.grade))


# 调用
s = student('ken', 10, 60, 3)
s.speak()
