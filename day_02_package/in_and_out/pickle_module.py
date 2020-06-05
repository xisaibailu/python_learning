"""
pickle模块实现了基本的数据序列和反序列化。
"""

###############序列化dump()###################
import pickle

# 使用pickle模块将数据对象保存到文件中
# data1 = {'a': [1, 2.0, 3, 4 + 6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}
# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)
#
# output = open('data.pkl', 'wb')
#
# # pickle dictionary using protocol 0
# pickle.dump(data1, output)
# # Pickle the list using the highest protocol available.
# pickle.dump(selfref_list, output, -1)
#
# output.close()

###################反序列化 load()#######################

import pprint,pickle
#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl','rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)
pkl_file.close()