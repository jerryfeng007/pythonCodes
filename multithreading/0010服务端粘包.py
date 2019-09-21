import socket
ip_port = ('localhost', 8090)
back_log = 5
buffer_size = 1024
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)
conn, addr = tcp_server.accept()

data1 = conn.recv(1)
print(data1)
# data2 = conn.recv(5)
# print(data2)
# data3 = conn.recv(1)
# print(data3)
# 这是第二种粘包，即：发送的数据比较多，但是一次接收的少，
# 所以下次再接收的时候，仍是上次未取完的数据
