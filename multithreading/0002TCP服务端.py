# 学习socket就是为了完成C/S架构的开发
# osi七层
# 网络通信原理：www.cnblogs.com/linhaifeng/articles/5937962.html
# socket是应用层与tcp/ip协议族通信的中间软件抽象层，它是一组接口
# 我们无需深入理解tcp/udp协议，socket已经为我们封装好了
# 我们只需要遵循socket的规定去编程，写出的程序自然就是遵循tcp/udp标准的

# 基于tcp协议的套接字编程
# recv在自己这端的缓冲区为空时，阻塞；recvfrom不会阻塞，会收空

import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('localhost', 8000))
phone.listen(5)  # backlog的值，服务器需要调试这个值是多少

print('等待客户端连接......')
conn, addr = phone.accept()  # 在这里等待客户端连接
# 服务端也可以主动发消息
msg = conn.recv(1024)
print('客户端发来的消息是：', msg.decode('utf8'))
conn.send(msg.upper())
conn.close()
phone.close()
