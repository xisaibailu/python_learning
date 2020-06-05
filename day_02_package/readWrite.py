####################读取#####################
# """
# 写入 write()
# """
# #打开一个文件
# f = open("./tmp/foo.txt","w")
# f.write("python is a good language!\n"
#         "good good study\n"
#         "day day up \n")
#
# #关闭文件
# f.close()
#
# """
# read() 读取
# 可输入参数size，如果size不填或为负，则读取全部内容
# """
# r = open("./tmp/foo.txt","r")
# str = r.read()
# print(str)
#
# #关闭文件
# r.close()
#
# """
# readline()
# 从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
#
# readlines()
# 返回该文件中包含的所有行
# """
# #打开文件
# fl=open("./tmp/foo.txt",'r')
# # str1 = fl.readline()
# # print("readline:",str1)
#
# str2=fl.readlines()
# print("readlines",str2)
#
# fl.close()
#

######################写入##############################
# f = open("./tmp/foo.txt","w")
# num = f.write("hahahahhaha\n.wakawakawaka\n")  #返回写入的字符数
# print(num)
# f.close()

#如果写入的不是字符串，需要先进行转换
# f = open("./tmp/foo.txt","w")
# value = ('www.runoob.com',14)
# print(type(value))
# s = str(value)
# f.write(s)
# print("返回文件对象指向的当前所处的位置：",f.tell())  #22，文件末尾
# f.close()

""""
f.seek(offset,from_what)
seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符
"""
f = open("./tmp/foo.txt","rb+")
num=f.write(b'0123456789abcdef')
print(num)
print(f.seek(5)) # 移动到文件的第六个字节
print(f.read(1))
print(f.seek(-3,2))# 移动到文件的倒数第三字节
print(f.read(1))