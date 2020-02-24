from  socket import *

host_port = ("127.0.0.1",3000)

s=socket(AF_INET,SOCK_DGRAM,0)
s.bind(host_port)

while(True):
    data,addr=s.recvfrom(1024)
    print("[+]Got connection from ",addr)
    print(data.decode('ascii'))
    msg="hi from server"
    s.sendto(msg.encode('ascii'),addr)
    break
s.close()
print("Closed")

