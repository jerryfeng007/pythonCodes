import threading
from time import sleep, ctime


def music():
    print('begin to listen', ctime())
    sleep(3)
    print('stop to listen', ctime())


def game():
    print('begin to play game', ctime())
    sleep(5)
    print('stop to play game', ctime())


threads = []
t1 = threading.Thread(target=music)
t2 = threading.Thread(target=game)
threads.append(t1)
threads.append(t2)

# t1.setDaemon(True)  # 守护线程，守护主线程，跟主线程同退，一定要在start方法之前设置
t2.setDaemon(True)
for t in threads:
    t.start()
# t.join()
    # print(t.getName())
    # print(threading.active_count())

print('ending..........')  # 主线程
