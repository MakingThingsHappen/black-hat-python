# -*- coding: utf-8 -*-
import socket

target_host = ''
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Because UDP is a connectionless protocol, there is no call to connect() beforehand


# send some data
client.sendto("DATA", (target_host, target_port))

# receive some date
data, addr = client.recvfrom(4096)
