import socket,threading,argparse
parser = argparse.ArgumentParser()
parser.add_argument('--host',default='localhost')
parser.add_argument('--port',type=int,default=5678)
args = parser.parse_args()
dit = {}
key = ''
value = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind((args.host,args.port))
s.listen(5)
print('等待连接中...')
def tcplink(sock, addr):
    print('正在连接 %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        c = str(data)
        d = c.strip("b")
        e = d.strip("'")
        b = e.split(" ")
        print(b)
        key = b[1]
        if b[0] == 'SET':
            value = b[2]
            dit[key] = value

        elif b[0] == 'GET':
            if  key in dit:
                sock.send(dit[key].encode())
            else :
                sock.send('\n'.encode())
        else :
            sock.send('请输入正确的命令：SET/GET'.encode())
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
