import socket
ip_port = ('localhost', 8092)
buffer_size = 1024
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.sendto('hello'.encode('utf8'), ip_port)  # 收发都是操作的自己的缓冲区
udp_server.sendto('world'.encode('utf8'), ip_port)  # 收发都是操作的自己的缓冲区
udp_server.sendto('egon'.encode('utf8'), ip_port)  # 收发都是操作的自己的缓冲区
