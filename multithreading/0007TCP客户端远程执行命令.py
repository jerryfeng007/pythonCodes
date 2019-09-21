import socket
ip_port = ('localhost', 8090)
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
    cmd_res = tcp_client.recv(buffer_size)
    print(cmd_res.decode('gbk'))  # 用什么编码，就要用什么解码

tcp_client.close()
#  如果quit的话，执行这一句，那么服务端会死循环，服务端必须加一个cmd为空的判断
