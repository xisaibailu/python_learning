import mysql.connector

#创建数据库连接
# mydb=mysql.connector.connect(
#   host="192.168.220.133",
#   user="root",
#   passwd="123456"
# )
#
# print(mydb)

#创建数据库
# mycursor = mydb.cursor()
# mycursor.execute("create database python_tab")

#输出所有数据库列表
# mycursor = mydb.cursor()
# mycursor.execute("show databases")
# for x in mycursor:
#   print(x)

"""
增删改查操作
"""
#创建数据表
mydb=mysql.connector.connect(
  host="192.168.220.133",
  user="root",
  passwd="123456",
  database="python_tab"
)

#显示数据库python_tab中的所有表
# mycursor = mydb.cursor()
# mycursor.execute("create table sites(name varchar(100),url varchar (100))")
# mycursor.execute("show tables")
# for x in mycursor:
#   print(x)

#添加表的Id为自主键
# mycursor = mydb.cursor()
# mycursor.execute("alter table sites add column id int not null auto_increment primary key")

#插入数据
# mycursor =mydb.cursor()
# sql="insert into sites(name,url) values (%s,%s)"
# val=("runoob","http://baidu.com")
# mycursor.execute(sql,val)
#
# mydb.commit() #数据内容有更新，必须使用该语句
#
# print(mycursor.rowcount,"条记录插入成功")

#批量插入 executemany(),第二个参数为元组列表
# mycursor = mydb.cursor()
# sql="insert into sites(name,url) values (%s,%s)"
# val=[
#   ("google","1"),
#   ("github","2"),
#   ("taobao","3"),
#   ("gitee","4")
# ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"条记录插入成功","ID:",mycursor.lastrowid)  #mycursor.lastrowid获取插入数据的ID

#查询数据
# mycursor= mydb.cursor()
# mycursor.execute("select * from sites")
# myresult = mycursor.fetchall()    #获取所有记录
# for x in myresult:
#   print(x)

#使用占位符防止sql注入
# mycursor = mydb.cursor()
# sql="select * from sites where name = %s"
# na=("google",)
#
# mycursor.execute(sql,na)
# myresult=mycursor.fetchall()
#
# for x in myresult:
#   print(x)

# mycursor = mydb.cursor()
# mycursor.execute("select * from sites limit 3 offset 1") #0为第一条，1为第二条。。。。
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)

#删除记录
# mycursor = mydb.cursor()
#
# sql="delete from sites where name =%s"
# na=("github",)
#
# mycursor.execute(sql,na)
# mydb.commit()
# print(mycursor.rowcount,"条记录删除")

#更新记录
mycursor = mydb.cursor()
sql="update sites set name=%s where name = %s"
val = ("zhihu","google")

mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"条记录更新")

#删除表
mycursor =mydb.cursor()
sql="drop table if exists sites" #删除数据表

mycursor.execute(sql)