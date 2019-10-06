# 秒表  ---------- 需要在控制台运行，才能使用 ctl + c
import time

# 方式1
# print('按下回车开始计时，按下CTL+C停止计时。')
#
# while True:
#     try:
#         input()
#         t1 = time.time()
#         print('开始')
#         while True:
#             time.sleep(1)
#             t = time.time()
#             tt = t - t1
#             print(round(tt), '秒')
#     except KeyboardInterrupt:
#         print('结束')
#         end = time.time()
#         print('总共的时间为:', round(end - t1), '秒')
#         break


# 方式2
print('按下回车开始计时，按下CTL+C停止计时。')

input()
t1 = time.time()
print('开始')

while True:
    try:
        time.sleep(1)
        t = time.time()
        tt = t - t1
        print(round(tt), '秒')
    except KeyboardInterrupt:
        print('结束')
        end = time.time()
        print('总共的时间为:', round(end - t1), '秒')
        break
