import socket 
import struct
import sys

def clientCode():
   
    sockServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)
    
    sockServer.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
   
    sockServer.bind(('',5007))

    
    mreq = struct.pack('=4sl',socket.inet_aton('224.1.1.1'),socket.INADDR_ANY)
    sockServer.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
     

   
    while True:
        try:
            data, address = sockServer.recvfrom(1024)
            print  ('Client 2: Data Received from', (address))
            print  ('and the Received Data is: ', data, '\n')
        except:
            print ("Client 2 timed out")

if __name__=='__main__':
    clientCode()