# import socket
# s=socket.socket()
# host=socket.gethostname()
# port=12345
# #s.connect(('192.168.0.107',12345))
# s.connect((host,port))
# while(1):
#     print(s.recv(1024))
#     #s.close()
#

import socket
s=socket.socket()
host=socket.gethostname()
port=12345
#s.connect(('192.168.0.107',12345))
s.connect((host,port))
while True:
    print(s.recv(1024))
    #while(1):
    n = input("enter the msg")
    #print('Connection', addr)
    s.send(bytes(n, encoding='utf8'))
    print("your msg is send to user")