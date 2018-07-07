'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.06.15
License:     GNU, see LICENSE for more details
Description:.
'''

import socket

def SendData(aHost, aPort = 80, aData = None):
    R = True
    try:
        Addr = socket.getaddrinfo(aHost, aPort)[0][-1]
        Sock = socket.socket()
        Sock.settimeout(1)
        Sock.connect(Addr)
        if (aData):
            Sock.sendall(aData)
            R = Sock.recv(512)
        Sock.close()
    except Exception as e:
        print('Error','SendData()', e)
        R = False
    return R
