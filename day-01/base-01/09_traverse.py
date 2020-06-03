"""
遍历技巧：
1.item（）,遍历字典中的键和值
2.enumerate（），遍历序列中的索引和对应的值
3.zip()，遍历两个或更多的序列
4.reversed()，反向遍历一个序列
5.sorted（），按顺序遍历一个序列
"""
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
  print("K=" + k, "V=" + v)

for i, v in enumerate(['tic', 'tac', 'toe']):
  print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
  print('what is your {0}? It is {1}'.format(q, a))

for i in reversed(range(1, 10, 2)):
  print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
  print(f)
