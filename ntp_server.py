from socket import *
import time
ip_port=('127.0.0.1',8080)
buffer_size=1024

udp_server=socket(AF_INET,SOCK_DGRAM)
udp_server.bind(ip_port)

while True:
    data,addr=udp_server.recvfrom(buffer_size)
    print(data)

    back_time=time.strftime('%Y-%m-%d %X')
    udp_server.sendto(back_time.encode('utf-8'),addr)