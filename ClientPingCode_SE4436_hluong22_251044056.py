import sys, time
from socket import *

#Sets the server host name, and the port number
host = "localhost"
port = 1500
#Timeout variable in seconds
timeout = 2
#Creates an internet domain socket where the type is a datagram-based protocol
clientsocket = socket(AF_INET, SOCK_DGRAM)
#Sets the reply/wait time to 2 seconds 
clientsocket.settimeout(timeout)

port = int(port)

ptime = 0

while (ptime<10):
    ptime +=1

    data = "Ping " + str(ptime) + " " + time.asctime()
    try:
        RTTb=time.time()
        clientsocket.sendto(data.encode(),(host, port))
        message, address = clientsocket.recvfrom(1024)
        RTTa = time.time()

        print ("Reply from " + address[0] + ": " + message.decode())
        print ("RTT: " + str(RTTa-RTTb))

    except:
        print ("Request timed out.")
        continue
clientsocket.close()