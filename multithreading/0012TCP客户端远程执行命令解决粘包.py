# low版解决方法
import socket
ip_port = ('localhost', 8091)
buffer_size = 1024

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    cmd = input('请输入命令:>>>').strip()  # 客户端有可能输入空数据
    if not cmd:
        continue
    if cmd == 'quit':
        break
    tcp_client.send(cmd.encode('utf8'))
    # 解决粘包
    length = tcp_client.recv(buffer_size)  # 接收length
    tcp_client.send(b'ready')  # 因为服务端的两个send间隔小，有可能会粘包，所以这里再send回去
    length = int(length.decode('utf8'))
    recv_size = 0
    recv_msg = b''
    while recv_size < length:
        data = tcp_client.recv(buffer_size)
        recv_msg = recv_msg + data
        recv_size = len(recv_msg)

    print(recv_msg.decode('gbk'))  # 用什么编码，就要用什么解码

tcp_client.close()  # 如果quit的话，执行这一句，那么服务端会死循环，服务端必须加一个cmd为空的判断
