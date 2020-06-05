"""
JSON 的编码和解码
json.dumps():对数据进行编码
json.loads():对数据进行解码

【python】       【JSON】
dict        ===  object
list、tuple ===  array
str         ===  string
int、float  ===  number
"""
import json

#dict 转换为json对象
data={
  'no':1,
  'name':'runoob',
  'url':'http:baidu.com'
}

json_str = json.dumps(data)
print("python 原始数据：",repr(data))
print("JSON对象：",json_str)
print(type(json_str))

#将JSON对象转换为dict
data2 = json.loads(json_str)
print("data2['name']",data2['name'])
print("data2['url']",data2['url'])

"""
如果要处理的是json文件
使用json.dump() 和json.load() 来编码和解码json数据
"""
#写入JSON数据
with open('./data.json','w') as f:
  json.dump(data,f)

#读取JSON数据
with open('./data.json','r') as f:
  data=json.load(f)
  print(data)
