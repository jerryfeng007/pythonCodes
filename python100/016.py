# 输出指定格式的日期
import time
t = time.localtime()
tt = time.strftime('%Y-%m-%d %H:%M:%S', t)
print(t)
print(tt)
