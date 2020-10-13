import datetime
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
#Change port into integer 
port = int(port)
#
pingTime = 0



#The following code will ping 10 times
while (pingTime<10):
    #Counter that counts up each time it has pinged
    pingTime +=1
    #Grabs the current date and time in YY/MM/DD H/M/S/MS format
    currentTime = datetime.datetime.now()
    #Creates the client message to be sent
    data = "Ping " + str(pingTime) + " " + str(currentTime)
    try:
       # RTTb=time.time()
        clientsocket.sendto(data.encode(),(host, port))
        message, address = clientsocket.recvfrom(1024)
        #RTTa = time.time()
        print ("Reply from " + address[0] + ": " + message.decode())
        print ("RTT: ")
        #RTTinfo=(RTTa-RTTb)

       # print ("RTT: "+ RTTinfo.microseconds)
    except:
        print ("Request timed out.")
        continue
clientsocket.close()