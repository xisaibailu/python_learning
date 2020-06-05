"""
日期和时间
time模块：
calendar模块：
"""
import time

ticks = time.time()  # 只能表示1970年---2038年
print("获取当前时间戳：", ticks)  # 1591335929.6008034

# 将时间戳转为日期元组
localtime = time.localtime(ticks)
print("本地时间为：", localtime)
# time.struct_time(tm_year=2020, tm_mon=6, tm_mday=5, tm_hour=13, tm_min=49, tm_sec=45, tm_wday=4, tm_yday=157, tm_isdst=0)

# 获取简单默认的格式化的日期
localtime_1 = time.asctime(time.localtime(time.time()))
print("简单日期格式的本地时间：", localtime_1)

# 获取指定格式的格式化日期
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 2020-06-05 13:55:41

print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))  # Fri Jun 05 13:58:11 2020

# 将格式字符串转换为时间戳
a = "Fri Jun 05 13:58:11 2020"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 获取某月月历
import calendar

cal = calendar.month(2020, 6)
print("以下输出2020年6月份的日历：")
print(cal)

#print(calendar.calendar(2020,w=2,l=1,c=6))

#进度条实例
import time

scale = 50

print("执行开始".center(scale//2,"-"))  # .center() 控制输出的样式，宽度为 25//2，即 22，汉字居中，两侧填充 -

start = time.perf_counter() # 调用一次 perf_counter()，从计算机系统里随机选一个时间点A，计算其距离当前时间点B1有多少秒。当第二次调用该函数时，默认从第一次调用的时间点A算起，距离当前时间点B2有多少秒。两个函数取差，即实现从时间点B1到B2的计时功能。
for i in range(scale+1):
    a = '*' * i             # i 个长度的 * 符号
    b = '.' * (scale-i)  # scale-i） 个长度的 . 符号。符号 * 和 . 总长度为50
    c = (i/scale)*100  # 显示当前进度，百分之多少
    dur = time.perf_counter() - start    # 计时，计算进度条走到某一百分比的用时
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')  # \r用来在每次输出完成后，将光标移至行首，这样保证进度条始终在同一行输出，即在一行不断刷新的效果；{:^3.0f}，输出格式为居中，占3位，小数点后0位，浮点型数，对应输出的数为c；{}，对应输出的数为a；{}，对应输出的数为b；{:.2f}，输出有两位小数的浮点数，对应输出的数为dur；end=''，用来保证不换行，不加这句默认换行。
    time.sleep(0.1)     # 在输出下一个百分之几的进度前，停止0.1秒
print("\n"+"执行结果".center(scale//2,'-'))