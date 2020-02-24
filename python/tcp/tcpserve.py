from socket import *

host = "127.0.0.1"
port = 3000

s=socket(AF_INET,SOCK_STREAM,0)
s.bind((host,port))

s.listen(5)

while(True):
    c,addr=s.accept()
    rmsg=c.recv(2048)
    print(rmsg.decode('ascii'))

    msg="msg from server"
    c.send(msg.encode('ascii'))

    break

s.close()
print("Closed")


