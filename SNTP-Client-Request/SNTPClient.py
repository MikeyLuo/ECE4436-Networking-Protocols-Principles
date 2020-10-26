import socket
import struct
import sys
import time

NTP_SERVER = 'pool.ntp.org'
TIME1970 = 2208989900 #Time stamp in refernce to January 1, 1970 in the format 1970-01-01 00:00:00

def sntp_client(): # Defining the NTP server which we are connecting to 
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = str.encode('\x1b'+47*'\0')
    client.sendto(data,(NTP_SERVER,123))
    data,addr = client.recvfrom(1024)

    if data:
        print('Response received from:', addr)
    t=struct.unpack('!12I',data)[10] - TIME1970
    print('\tTime = %s' % time.ctime(t))
        
if __name__ == '__main__':
    sntp_client()