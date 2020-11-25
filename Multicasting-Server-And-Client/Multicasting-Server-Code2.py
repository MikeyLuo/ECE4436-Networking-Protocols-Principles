import socket 
import struct
import sys
import time


def serverCode():

   
    multicast_group = ('224.1.1.1',5007) 

    sockServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) 
    sockServer.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)  
      
    sockServer.settimeout(3)

    while True:
        sockServer.sendto(b' Multicasting Assignmnet ECE 4436/9303 from server 2 ', multicast_group)
        print  ('Server 2: multicast packet is sent now')
        time.sleep(3)

if __name__=='__main__':
    serverCode()