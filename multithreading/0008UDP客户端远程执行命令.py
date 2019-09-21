# udp不依赖哪个服务端，不基于连接，客户端自己也能运行,可以发，但是没人收，所以客户端会卡住，发的这一条也就丢了
# 所以udp不可靠，不管对方有没有收到，只管发
#tcp是可靠的，不能只运行客户端
import socket
ip_port = ('localhost', 8091)
buffer_size = 1024
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    cmd = input('请输入命令:>>>').strip()  # 客户端有可能输入空数据
    if not cmd:
        continue
    if cmd == 'quit':
        break
    udp_client.sendto(cmd.encode('utf8'), ip_port)
    cmd_res, addr = udp_client.recvfrom(buffer_size)
    print(cmd_res.decode('gbk'))

udp_client.close()