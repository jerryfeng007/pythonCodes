# tcp
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('conn is ', self.request)  # conn
        print('addr is ', self.client_address)  # addr
        while True:
            try:
                data = self.request.recv(1024)
                if not data:
                   break
                print('收到客户端的消息是', data, self.client_address)
                self.request.sendall(data.upper())
            except Exception as e:
                break


if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(('localhost', 8094), MyServer)
    s.serve_forever()