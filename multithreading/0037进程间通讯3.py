# 通讯方法3：Managers
import multiprocessing


def f(d, l, n):
    d[n] = '1'  # 第一个进程，{0:'1'}  第二个进程 {0:'1',1:'1'} 第三个进程{0:'1',1:'1'，2:'1'}
    d['2'] = 2  # 第一个进程 {0:'1','2':2}  第二个进程 {0:'1',1:'1','2':2}
    l.append(n)  # 第一个进程 [0,1,2,3,4,0]  第二个进程 [0,1,2,3,4,0,1]
    print(l)
    # print('son process:', id(d), id(l))


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:  # with，上下文管理，
                                                # 例如以前的with open() as f，不用写close了
        d = multiprocessing.Manager().dict()  # 空字典
        l = multiprocessing.Manager().list(range(5))  # [0,1,2,3,4]
        # print('main process:', id(d), id(l))
        p_list = []
        for i in range(10):
            p = multiprocessing.Process(target=f, args=(d, l, i))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()
        print(d)  # 子进程里修改之后，这里主进程打印
        print(l)  # 子进程里修改之后，这里主进程打印
