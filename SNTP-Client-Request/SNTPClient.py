import socket
import struct
import sys
import time

#NTP_SERVER =
TIME1970 = 2208989900 #Time stamp in refernce to January 1, 1970 in the format 1970-01-01 00:00:00

def sntp_client(host="pool.ntp.org"): # Defining the NTP server which we are connecting to 
 ''' Fill in start 

    let variable data contain the received data
    let address be the address that the NTP replied from 
    
Fill in end'''

    if data:
        print('Response received from:', address)
        
'''Fill in start

        in this part you have to calculate the time
       let variable t be the final time you calculated  

Fill in end'''
        #print ('\tTime=%s' % time.ctime(t))
if __name__ == '__main__':
    sntp_client()