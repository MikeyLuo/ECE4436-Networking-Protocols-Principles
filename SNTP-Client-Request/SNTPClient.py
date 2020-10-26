import socket
import struct
import sys
import time

NTP_SERVER = 'pool.ntp.org' # Setting the server address to which we are connecting to
TIME1970 = 2208988800 # NTP Time stamp in refernce to January 1, 1970 in the format 2,208,988,800

def sntp_client(): # NTP function
    # Creates an internet domain socket where the type is a datagram-based protocol
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    # Encoding the SNTP protocol data packet
    data = str.encode('\x1b'+47*'\0')
    # Client sends the encoded data
    client.sendto(data,(NTP_SERVER,123))
    # Grab the data, and the address of where the data was received from
    data,address = client.recvfrom(1024)

    # If data has been received from the server do the following
    if data:
        # 'struct' unpacks the data received from the local server
        currenTime=struct.unpack('!12I',data)[10] 
        # Subtracts the time the data was received from the refernce time to get real time
        currenTime=currenTime - TIME1970
        # Prints the address where the data was received from
        print('Response received from:', address)
        # Prints the real time of when the data was received
        print('\tTime= %s' % time.ctime(currenTime))
# Seeting the value of __name__ attribute to __main__ 
if __name__ == '__main__':
    sntp_client()