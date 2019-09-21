import socket
ip_port = ('127.0.0.1', 8090)
buffer_size = 1024
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('>>>>>>>').strip()
    udp_client.sendto(msg.encode('utf8'), ip_port)  # 需要加上服务端的ip和端口
    data, addr = udp_client.recvfrom(buffer_size)
    print('ntp服务器的标准时间是', data.decode('utf8'))
