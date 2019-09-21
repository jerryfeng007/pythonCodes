#
# # 先进后出(后进先出)
# import queue
# q = queue.LifoQueue()
# q.put(12)
# q.put('hello')
# q.put({'name': 'yuan'})
#
# while 1:
#     data = q.get()
#     print(data)


# 优先级
import queue
q = queue.PriorityQueue(3)
q.put([3, 12])
q.put([2, 'hello'])
q.put([4, {'name': 'yuan'}])
# q.put_nowait(21)  # 相当于是q.put(block=False)
print(q.empty())
print(q.full())
print(q.qsize())

while 1:
    data = q.get()
    data = q.get_nowait()  # 相当于q.get(block=False)
    # print(data)
    print(data[1])

# 队列的其他方法，除了put 和 get
# q.qsize()
# q.empty()
# q.full()
# q.put_nowait()
# q.get_nowait()
# q.task_done() 向任务已经完成的队列发送一个信号, 和下面的join是一对
# q.join() 实际上意味着等到队列为空，再执行别的操作
