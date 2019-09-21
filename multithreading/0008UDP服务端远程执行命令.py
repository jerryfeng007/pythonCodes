# tcp会有粘包现象
# 但udp是没有的，他只管发，如果发的多，收的少，没收到的就丢了，可以把buffersize改大一些
# 粘包，比如输入dir输出正确的内容，再输入ipconfig仍输出dir的内容
# 有粘包现象是因为buffersize只收了1024，没收干净，下次输出时仍输出了以前的内容
import socket
import subprocess
ip_port = ('localhost', 8091)
buffer_size = 1024
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(ip_port)

while True:
    cmd, addr = udp_server.recvfrom(buffer_size)
    print('收到客户端的命令', cmd.decode('utf8'))
    # 运行这条命令，发送结果给客户端
    res = subprocess.Popen(cmd.decode('utf8'), shell=True,
                           stderr=subprocess.PIPE, # 错误的管道
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE)  # 标准输出管道
    # 命令运行时有可能会报错
    err = res.stderr.read()  # 从错误的管道读取数据
    if err:  # 如果运行出错，错误的管道必定不为空
        cmd_res = err
    else:
        cmd_res = res.stdout.read()  # 读取标准输出管道的数据
    if not cmd_res:  # 加这个判断，是因为类似cd ..这样的命令，没有返回数据
        udp_server.sendto('执行成功'.encode('gbk'), addr)
    udp_server.sendto(cmd_res, addr)  # bytes
