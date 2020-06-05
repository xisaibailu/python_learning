"""
利用numpy 、 pandas 进行excel数据分析
思路：
1.对于All表 ：取出有用字段，处理缺失值，数据透视
2.对于sf和sfweibo表：以省份名做数据连接成sf_sfweibo，并与All表做数据连接sf_sfweibo_all
3.对于base_info表：与sf_weibo_all表做数据连接，计算h值，处理数据，计算相关性
4.导出最后结果到execl文件中
"""
#1.all表数据处理
