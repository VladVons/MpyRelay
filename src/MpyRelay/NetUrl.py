'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.06.14
License:     GNU, see LICENSE for more details
Description: 
'''

import socket
#
from NetHttpHead import GetHttpHead  

def _Load(aUrl, aPort, aStream, aR):
    #print('---0', aUrl, aPort)
    try:
        _, _, Host, Path = aUrl. split('/', 3)
        Addr = socket.getaddrinfo(Host, aPort)[0][-1]
        Sock = socket.socket()
        Sock.connect(Addr)
    except Exception as e:
        print('_Load', e)
        return

    Data = bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (Path, Host), 'utf8')
    Sock.send(Data)

    Head = GetHttpHead(Sock)
    if (not Head):
        return

    HeadReq = Head.get('head')
    Arr  = HeadReq.split(' ')
    if (len(Arr) < 2) or (Arr[1] != '200'):
        return

    Len = int(Head.get('content-length', 0))
    if (Len > 0):
        while True:
            Data = Sock.recv(256)
            if (not Data):
                break

            Data = Data.decode("utf-8")
            if (aStream):
                aR += aStream.write(Data)
            else:
                aR += Data
    Sock.close()
    return aR


def LoadToStream(aUrl, aPort, aHFile):
    return _Load(aUrl, aPort, aHFile, 0)

def LoadToStr(aUrl, aPort = 80):
    return _Load(aUrl, aPort, None, '')
