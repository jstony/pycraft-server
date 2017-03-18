"""
MinecraftServer
- Minecraft Server written in Python :)
"""
import socket
import sys
import os
from util import Logger

HOST = ''
PORT = 25565

SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCK.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    SOCK.bind((HOST, PORT))
    os.system('clear')
    print Logger().success('Server is listening on port :' + str(PORT))
except socket.error as msg:
    print Logger().error('Bind failed. Error code: ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

SOCK.listen(10)

while 1:
    CONN, ADDR = SOCK.accept()
    print Logger().success('Connected with ' + ADDR[0] + ':' + str(ADDR[1]))

SOCK.close()
