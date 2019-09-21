import socket
ip_port = ('localhost', 8090)
buffer_size = 1024
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.connect(ip_port)
tcp_server.send('hello'.encode('utf8'))  # 收发都是操作的自己的缓冲区
tcp_server.send('world'.encode('utf8'))
tcp_server.send('egon'.encode('utf8'))
