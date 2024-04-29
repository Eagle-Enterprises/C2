####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
####################################################

# Imports
# Requires install of python, pyserial (i.e. pip instal pyserial)
import socket

UDP_IP = "localhost"
UDP_PORT = 14550

sock = socket.socket(socket.AF_INET, # Internet
   socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
   data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
   print("received message: %s" % data)