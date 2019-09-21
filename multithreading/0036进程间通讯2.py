# 通讯方法2：管道 Pipe
import multiprocessing


def f(conn):
    conn.send([12, {'name':'yuan'}, 'hello'])  # 子进程发送
    response = conn.recv()  # 子进程接收
    print('response', response)
    conn.close()
    # print('q_ID2:', id(conn))


if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()  # 这里是双向管道，之前学的conn也是
    # 双向管道就是：你给我发消息，你还可以接收我的消息
    # 这是主进程生成的两个管道对象，要想主进程和子进程通信，需要先传给子进程
    # print('q_ID1:',id(child_conn))
    p = multiprocessing.Process(target=f, args=(child_conn,))
    p.start()  # 主进程与子进程通信

    print(parent_conn.recv())  # 主进程接收
    parent_conn.send('儿子你好！')  # 主进程发送
    p.join()
