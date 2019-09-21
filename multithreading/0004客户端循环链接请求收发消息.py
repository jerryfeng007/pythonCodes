import socket
ip_port = ('localhost', 8090)
back_log = 5  # 能挂起的连接数
buffer_size = 1024  # 接收的字节
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    msg = input('>>>>>>').strip()  # 去掉字符串首位指定的字符，这里是空格或回车
    if not msg:
        continue
    tcp_client.send(msg.encode('utf8'))
    print('客户端已经发送消息')
    data = tcp_client.recv(buffer_size)
    print('收到服务端发来的消息', data.decode('utf8'))
