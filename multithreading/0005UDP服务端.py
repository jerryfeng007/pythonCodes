# udp套接字
# recv在自己这端的缓冲区为空时，阻塞；recvfrom不会阻塞，可以收空
import socket
ip_port = ('127.0.0.1', 8090)
buffer_size = 1024
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(ip_port)
# 因为客户端无需连接，所以这里也无需accept
while True:
    data, addr = udp_server.recvfrom(buffer_size)
    print(data.decode('utf8'))
    udp_server.sendto(data.upper(), addr)  # addr为客户端的ip和端口
