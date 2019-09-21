# tcp会有粘包现象,但udp是没有的；
# 粘包，比如输入dir输出正确的内容，再输入ipconfig仍输出dir的内容
# 有粘包现象是因为buffersize只收了1024，没收干净，下次输出时仍输出了以前的内容
import socket
import subprocess
ip_port = ('localhost', 8090)
back_log = 5
buffer_size = 1024
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)
while True:
    conn, addr = tcp_server.accept()
    print('新的客户端连接', addr)
    while True:
        try:  # 客户端非正常关闭的异常处理
            cmd = conn.recv(buffer_size)  # 服务器收到一条命令
            if not cmd:  # 这个判断是解决，输入quit时客户端的tcp_client关闭，这里会一直死循环打印
                break  # 这里是beak 不是 continue, 否则客户端quit之后，再连接时，不会重新accept
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
            if not cmd_res:  # 加这个判断，是因为类似cd ..这样的命令，没有返回数据,程序会卡住
                conn.send('执行成功'.encode('gbk'))
            conn.send(cmd_res)  # bytes
        except Exception as e:
           break
    conn.close()
