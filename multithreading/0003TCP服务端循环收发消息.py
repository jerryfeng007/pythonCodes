# recv在自己这端的缓冲区为空时，阻塞；recvfrom不会阻塞，会收空
import socket
ip_port = ('localhost', 8090)
back_log = 5  # 能挂起的连接数
buffer_size = 1024  # 接收的字节

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

print('服务端开始运行了')
conn, addr = tcp_server.accept()  # 服务端阻塞在这个位置，等待客户端连接，只要连接上就往下走
print('双向连接是：', conn)
print('客户端地址：', addr)

while True:
    data = conn.recv(buffer_size)  # recv在自己这端的缓冲区为空时，阻塞；recvfrom不会阻塞，会收空
    print('客户端发来的消息是', data.decode('utf8'))
    conn.send(data.upper())
