# import socket
# s=socket.socket()
# host=socket.gethostname()
# #print(s)
# #print(host)
# port=12345
# s.bind((host, port))
# s.listen(5)
# while True:
#     c,addr=s.accept()
#     while True:
#         n = input("enter the name")
#         print('Connection',addr)
#         #c.send(bytes("Welcome to python",encoding='utf8'))
#         c.send(bytes(n, encoding='utf8'))
#     #c.close()
#

import socket
s=socket.socket()
host=socket.gethostname()
#print(s)
#print(host)
port=12345
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print('Connection', addr)
    while True:
        n = input("enter the msg")
        c.send(bytes(n, encoding='utf8'))
        print("your msg is send to user")
        print(c.recv(1024))

    #c.close()