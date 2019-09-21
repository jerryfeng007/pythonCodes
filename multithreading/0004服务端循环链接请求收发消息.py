import socket
ip_port = ('localhost', 8090)
back_log = 5  # 能挂起的连接数
buffer_size = 1024  # 接收的字节
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

while True:  # 外层的while是接收多个连接
    print('服务端开始运行了')
    conn, addr = tcp_server.accept()  # 服务端阻塞在这个位置，等待客户端连接，只要连接上就往下走
    print('双向连接是：', conn)
    print('客户端地址：', addr)
    while True:  # 内层的while，跟这一个连接循环收发消息
        try:  # 加这个的目的，就是为了防止客户端断开的时候，服务器不会报错，要不然下一个客户端就没办法链接了
            data = conn.recv(buffer_size)
            print('客户端发来的消息是', data.decode('utf8'))
            conn.send(data.upper())
        except Exception as e:
            break  # 如果break，就跳出了内层循环，直接执行下面的conn.close()
    conn.close()
