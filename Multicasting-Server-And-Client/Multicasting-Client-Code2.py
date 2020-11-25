import socket 
import struct
import sys

def clientCode():
    #multicast_group = '192.168.0.27'
    #erverAddy = ('',5000)

    # Create the socket
    sockServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)
     # flag to tell the program to resuse a local socket so it doesn't have to wait for the timeout
    sockServer.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
    # Bind the socket to the server address 
    sockServer.bind(('',5007))

    # Tell program to add the socket created to the multicast group
    #group = socket.inet_aton(multicast_group)
    mreq = struct.pack('=4sl',socket.inet_aton('224.1.1.1'),socket.INADDR_ANY)
    sockServer.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
     

    # check for recevied data and then respond
    while True:
        try:
            data, address = sockServer.recvfrom(1024)
            print  ('Client 2: Data Received from', (address))
            print  ('and the Received Data is: ', data, '\n')
        except:
            print ("Client 2 timed out")

if __name__=='__main__':
    clientCode()