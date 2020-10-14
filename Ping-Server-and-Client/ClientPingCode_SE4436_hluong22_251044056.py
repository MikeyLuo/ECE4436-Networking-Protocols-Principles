import datetime
import time
from socket import *

#Sets the server host name, and the port number
host = "localhost"
port = 1500
#Timeout variable in seconds
timeout = 2
#Creates an internet domain socket where the type is a datagram-based protocol
clientsocket = socket(AF_INET, SOCK_DGRAM)
#Sets the reply/wait time of the client to 2 seconds 
clientsocket.settimeout(timeout)
#Change port into integer 
port=int(port)
#Setting ping counter to zero
pingCounter=0
average=[]
#The following code will ping 10 times
for i in range (0,10,1):
    #Counter that counts up each time it has pinged
    pingCounter+=1
    #Grabs the current date and time in YY/MM/DD H/M/S/MS format
    currentTime=datetime.datetime.now()
    #Creates the client message to be sent
    sendData = "Ping from client #" + str(pingCounter) + " " + str(currentTime)
    try:
        #Grabbing the current time of when packet is sent
        timeOne=time.time()
        #Send the encoded UDP packet to the server with the ping message
        clientsocket.sendto(sendData.encode(),(host, port))
        #Grabs the response from the server
        message, address = clientsocket.recvfrom(1024)
        #Grabbing the current time of when packet has been received
        timeTwo=time.time()
        """print ("Reply from " + address[0] + ": " +)""" 
        print(message.decode())
        RTT=(timeTwo-timeOne)*1000
        print ("> RTT Client #"+str(pingCounter)+": "+str(RTT)+" ms")
        if(RTT>0):
            average.append(RTT)    
    except:
        print ("Request timed out")
        continue
print("~ The Minimum RTT is: "+str(min(average))+" ms")
print("~ The Maximum RTT is: "+str(max(average))+" ms")
print("~ The Average RTT is: "+str((sum(average))/(len(average)))+" ms")
#print("~ The Standard Deviation RTT is: "+str())
clientsocket.close()