import socket
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(('localhost', 8094))
while True:
    msg = input('input>>>>').strip()
    if not msg:
        continue
    if msg == 'quit':
        break
    tcp_client.send(msg.encode('utf8'))
    data = tcp_client.recv(1024)
    print('收到服务端发来的消息', data.decode('utf8'))
tcp_client.close()
