import socket
ip_port = ('localhost', 8090)
back_log = 5
buffer_size = 1024
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)
conn, addr = tcp_server.accept()

data1 = conn.recv(buffer_size)  # 收发都是操作的自己的缓冲区  # 一次就收完了客户端发的3个
# data1 = conn.recv(5)  # 收指定长度的
print(data1)
data2 = conn.recv(buffer_size)  # 收发都是操作的自己的缓冲区
# data2 = conn.recv(5)
print(data2)
data3 = conn.recv(buffer_size)  # 收发都是操作的自己的缓冲区
# data3 = conn.recv(4)
print(data3)

'''第一个recv全部收到三条，第二第三收到为空（没有卡住），是因为客户端连接断开所致
b'helloworldegon'
b''
b''
'''
# 这是第一种粘包，发送端多次发送，且间隔比较小，数据量少，合在一起了；
# 为啥会粘包， 是因为服务端压根儿不知道应该会收多少
# 可以指定 data1 = conn.recv(5)   data2 = conn.recv(5)    data3 = conn.recv(4)
