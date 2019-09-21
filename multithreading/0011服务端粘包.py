# udp不粘包
import socket
ip_port = ('localhost', 8092)
buffer_size = 1024
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(ip_port)
# data1, addr = udp_server.recvfrom(buffer_size)  # 一个recvfrom对应客户端一个send
# print(data1)
'''
data1, addr = udp_server.recvfrom(buffer_size)  # 对应客户端第一个send
print(data1)
data2, addr = udp_server.recvfrom(buffer_size)  # 对应客户端第2个send
print(data2)
data3, addr = udp_server.recvfrom(buffer_size)  # 对应客户端第3个send
print(data3)
'''
data1, addr = udp_server.recvfrom(1)  # 对应客户端第一个send, 只收到1，其他的丢了
print(data1)
data2, addr = udp_server.recvfrom(1)  # 对应客户端第2个send， 只收到1，其他的丢了
print(data2)
data3, addr = udp_server.recvfrom(2)  # 对应客户端第3个send， 只收到2，其他的丢了
print(data3)
