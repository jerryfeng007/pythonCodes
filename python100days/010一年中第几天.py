# 计算指定的年月日是这一年的第几天。

import time
print(time.localtime())

# 结果中的280就是
# time.struct_time(tm_year=2019, tm_mon=10, tm_mday=7, tm_hour=19, tm_min=29, tm_sec=10, tm_wday=0,
# tm_yday=280, tm_isdst=0)


# 给定一个日期
s = '2016-12-31'

# 转化为时间元组
t = time.strptime(s, '%Y-%m-%d')
print(t)

# 结果中的281就是
# time.struct_time(tm_year=2016, tm_mon=10, tm_mday=7, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4,
# tm_yday=281, tm_isdst=-1)
