from socket import *

host_port=("127.0.0.1",3000)

s=socket(AF_INET,SOCK_DGRAM,0)

msg="Client sez gat a job"
s.sendto(msg.encode('ascii'),host_port)

data,addr=s.recvfrom(1024)

print(data.decode('ascii'))

s.close()
