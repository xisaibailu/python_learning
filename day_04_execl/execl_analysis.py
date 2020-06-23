"""
利用numpy 、 pandas 进行excel数据分析
思路：
1.对于All表 ：取出有用字段，处理缺失值，数据透视
2.对于sf和sfweibo表：以省份名做数据连接成sf_sfweibo，并与All表做数据连接sf_sfweibo_all
3.对于base_info表：与sf_weibo_all表做数据连接，计算h值，处理数据，计算相关性
4.导出最后结果到execl文件中
"""
# 1.all表数据处理
from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import randn
from pandas import Series, DataFrame
from datetime import datetime
import xlrd, openpyxl

xlsx_file = pd.ExcelFile('./test1.xlsx')
All = xlsx_file.parse('All')

# 取出有用字段，删除无用列
d1 = All.drop(All.columns[:11], axis=1, inplace=False)
All = d1.drop(d1.columns[-1], axis=1, inplace=False)

# 显示表格前五行
All.head(5)

len(All)
# 删除重复项
All[All.duplicated() == True].index[:20]
All.drop_duplicates(inplace=True)
# 处理缺失值
All[u'转发数'][All[u'转发数'] == u'转发'] = '0'
All[u'评论数'][All[u'评论数'] == u'评论'] = '0'
All[u'点赞数'][All[u'点赞数'] == u'赞'] = '0'
# 数据透视
All.describe()
# 查看表中各个列的数据类型
All.dtypes

# 将DataFrame表中的某列数据进行转换类型
All[u'转发数'] = All[u'转发数'].astype('int64')

All[u'评论数'] = All[u'评论数'].astype('int64')

All[u'点赞数'] = All[u'点赞数'].astype('int64')

# 将预处理的表保存到All.xlsx中
All.to_excel('All.xlsx', index=False)

# 将处理好的All.xlsx表生成透视表
All_pivot = All.pivot_table(values=[u'转发数', u'评论数', u'点赞数', u'微博内容'], index=[u'用户名'], \
                            aggfunc={u'转发数': np.sum, u'评论数': np.sum, u'点赞数': np.sum, u'微博内容': np.size})

# 给该列换名字
All_pivot.rename(columns={u'微博内容': u'当月总微博数'}, inplace=True)

# 将完成的透视表保存
All_pivot.to_excel('All_pivot.xlsx')

########以省份名做数据连接成sf_sfweibo###########
# 读取test1.xlsx中的sfbiao
sf = xlsx_file.parse('sf')

# 读取test1.xlsx中的sfweibo表
sfweibo = xlsx_file.parse('sfweibo')
# sfweibo.head()

sf[u'省份前两字'] = np.nan

for i in range(len(sf[u'省份名'])):
  sf[u'省份前两字'][i] = sf[u'省份名'][i][:2]

sfweibo[u'省份前两字'] = np.nan

for i in range(len(sfweibo[u'省份名'])):
  sfweibo[u'省份前两字'][i] = sfweibo[u'省份名'][i][:2]

# 保存数据
sf.to_excel('sf.xlsx', index=False)
sfweibo.to_excel('sfweibo.xlsx', index=False)

# 连接两表
sf_sfweibo = sf.merge(sfweibo, on=u'省份前两字')
# sf_sfweibo.head()

sf_sfweibo1 = sf_sfweibo.iloc[:, [4, 1, 2]]
# sf_sfweibo1.head()

# 存储连接后的表
sf_sfweibo1.to_excel('sf_sfweibo.xlsx', index=False)

################# 与All表做数据连接 sf_sfweibo_All #################
# 连接sf_sfweibo 和 All_pivot两表
sfweibo = sf_sfweibo1
sf_sfweibo_All_pivot = pd.merge(sf_sfweibo, All_pivot, left_on=u'微博用户名', right_on=u'用户名', right_index=True)
# sf_sfweibo_All_pivot.head()
# 将连接后的表进行存储
sf_sfweibo_All_pivot.to_excel('sf_sfweibo_All_pivot.xlsx', index=False)

# 与sf_weibo_All 做数据连接
# 处理用户的基本信息表base_info
base = xlsx_file.parse('base_info')
# 将base表与sf_sfweibo_All_pivot进行连接
sf_sfweibo_All_pivot_base = base.merge(sf_sfweibo_All_pivot, left_on=u'昵称', right_on='微博用户名')
ssapb = sf_sfweibo_All_pivot_base

ssapb.rename(columns={u'当月总微博数_x': u'当月总微博数'}, inplace=True)
# 删除其中多余的列
ssapb = ssapb.drop([u'昵称', u'当月总微博数_y'], axis=1)
# ssapb.iloc[0]
# 添加一列 当月原创数
ssapb[u'当月原创数'] = ssapb[u'当月总微博数'] - ssapb[u'当月转发数']

# 将某列同时与某段字符串连接，通过观察网页可以发现这是网址的特点
linkfix = "?is_ori=1&is_forward=1&is_text=1&is_pic=1&is_video=1&is_music=1&is_\
article=1&key_word=&start_time=2017-05-01&end_time=2017-05-31&is_search=1&is_searchadv=1#_0"

ssapb[u'当月博文网址'] = ssapb[u'主页链接'] + linkfix

allfix = "?profile_ftype=1&is_all=1#_0"
ssapb[u'全部博文网址'] = ssapb[u'主页链接'] + allfix

#计算出篇均转发/点赞/评论，并添加列
ssapb[u'篇均点赞']= ssapb[u'点赞数']/ssapb[u'当月总微博数']
ssapb[u'篇均转发'] = ssapb['转发数']/ssapb[u'当月总微博数']
ssapb[u'篇均评论'] = ssapb[u'评论数']/ssapb[u'当月总微博数']

#读取表中第一行数据
# ssapb.iloc[0]
#存储表格
ssapb.to_excel('sspab.xlsx',index=False)



