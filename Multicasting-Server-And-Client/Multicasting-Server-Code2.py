import socket 
import struct
import sys


def serverCode():

    #message = input(b' Multicasting Assignmnet ECE 4436/9303 from server 1 ') # creating the message that server will send
    multicast_group = ('224.1.1.1',5007) # setting the IP address and port number

    sockServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # creating the datagram socket
    sockServer.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255) # setting the data packet TTL for each message 
    # set timeout to 3 seconds so program knows how many responses to expect
    sockServer.settimeout(3)

   
    #try:
        # checks for any responses from all the clients
    while True:
        sockServer.sendto(b' Multicasting Assignmnet ECE 4436/9303 from server 1 ', multicast_group)
        print  ('Server 2: multicast packet is sent now')
        #try: # if there is a response, receive the data
        #data, server = sockServer.recvfrom(1024)
            #except socket.timeout: # if there is no reponse within 3 seconds, close the socket
                #print  ('timed out, no more responses')
                #break
            #else:
        print ('Server 2: multicast packet is sent now')
    #finally: # close the socket
        #print ('closing socket')
        #sockServer.close() # close the socket

if __name__=='__main__':
    serverCode()