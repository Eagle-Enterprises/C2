####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
####################################################

# Imports
# Requires install of python, pyserial (i.e. pip instal pyserial)
import socket

# mavproxy --master=tcp:localhost:5762 --out udp:localhost:14550

TCP_IP = "localhost"
TCP_PORT = 5763

sock = socket.socket(socket.AF_INET, # Internet
   socket.SOCK_STREAM) # TCP
sock.connect((TCP_IP, TCP_PORT))
sock.listen(5)


while True:
   data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
   print("received message: %s" % data)