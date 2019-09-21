# 基于udp实现ntp服务
# 写一个时间服务器！！！！！！！！！！！！！！
import time
import socket
ip_port = ('127.0.0.1', 8090)
buffer_size = 1024
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(ip_port)
while True:
    data, addr = udp_server.recvfrom(buffer_size)
    print(data.decode('utf8'))
    # current_time = time.ctime()
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    udp_server.sendto(current_time.encode('utf8'), addr)

# while True:
#     data, addr = udp_server.recvfrom(buffer_size)
#     print(data.decode('utf8'))
#
#     if not data:
#         format = '%Y-%m-%d %X'  # X 就是分钟小时秒
#     else:
#         format = data.decode('utf8')
#
#     current_time = time.strftime(format)
#     # current_time = time.ctime()
#     # current_time = time.strftime('%Y-%m-%d %H:%M:%S')
#     udp_server.sendto(current_time.encode('utf8'), addr)  # addr为客户端的ip和端口
#                                                           # 如果不是字符串，先转为字符串再用encode
