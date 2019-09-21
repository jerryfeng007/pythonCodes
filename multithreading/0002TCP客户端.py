import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('localhost', 8000))  # 客户端只要一连接，客户端就会accept
phone.send('hello'.encode('utf8'))  # 字符串编码成二进制
data = phone.recv(1024)
print('收到服务端发来的消息', data.decode('utf8'))
phone.close()
