import socket 
import struct
import sys
import time


def serverCode():

    #message = input(b' Multicasting Assignmnet ECE 4436/9303 from server 1 ') # creating the message that server will send
    multicast_group = ('224.1.1.1',5007) # setting the IP address and port number

    sockServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # creating the datagram socket
    sockServer.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255) # setting the data packet TTL for each message 
    # set timeout to 3 seconds so program knows how many responses to expect
    sockServer.settimeout(3)

   
   
    # checks for any responses from all the clients
    while True:
        sockServer.sendto(b' Multicasting Assignmnet ECE 4436/9303 from server 2 ', multicast_group)
        print  ('Server 2: multicast packet is sent now')
        time.sleep(3)

if __name__=='__main__':
    serverCode()