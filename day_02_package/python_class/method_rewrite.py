class parent:
  def myMethod(self):
    print("调用父类方法")


class child(parent):
  def myMethod(self):
    print("调用子类方法")

  def __myPrivateMethod(self):
    print("这个是我的私有方法")


# 调用
c = child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法
c.myPrivateMethod()  # 报错，外部不能调用私有方法
