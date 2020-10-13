import random 
from socket import *

#Assigning a server port nubmer 
serverPort = 1500
#Creates an internet domain socket where the type is a datagram-based protocol
serverSocket = socket(AF_INET, SOCK_DGRAM)
#Giving the socket an IP address, and a port nubmer
serverSocket.bind(('',serverPort))

while True: 
    #Generates a random number from 0 to 10
    rand = random.randint(0,10)
    #Receives the packet that the client sends, along with the address it is being sent from
    message,address = serverSocket.recvfrom(1024)
    #Capitalizes the message received from client
    message = message.upper()

    if rand<=3: #If this statement returns true, then the server will information back to the client
        continue
    serverSocket.sendto(message,address) #Send message to client
