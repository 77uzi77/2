import socket,argparse
parser = argparse.ArgumentParser()
parser.add_argument('--host',default='localhost')
parser.add_argument('--port',type=int,default=5678)
args = parser.parse_args()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect((args.host,args.port))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
while(True):
    try:
        data = input()
        if 'SET' in data:
            s.send(bytes(data,encoding=('utf-8')))
        elif 'GET' in data:
            s.send(bytes(data,encoding=('utf-8')))
            print(s.recv(1024).decode())
        elif 'END' in data:
            print('结束连接')
            break
        else :
            print('请输入正确的命令：SET/GET')
            print('如想断开连接，请输入：END')
    except ConnectionError:
        print("连接服务器失败...请重新连接")
s.send(b'exit')
s.close()
