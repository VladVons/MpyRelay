'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.06.03
License:     GNU, see LICENSE for more details
Description: 
'''

#MQTT
#http://icircuit.net/building-iot-application-using-esp32-micropython-10-steps/2077

import socket
import time
#
from Log         import Log
from NetHttpHead import GetHttpHead
from Lib         import CallTry


class THttpServer():
    def DoTimeout(self):
        pass

    def DoGet(self, aData):
        pass

    def Connect(self, aPort = 8080, aTimeOut = 1):
        Sock = socket.socket()
        Sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if (aTimeOut >= 0):
            Sock.settimeout(aTimeOut)

        Sock.bind(('', aPort))
        print('Bind socket port', aPort)

        Sock.listen(1)
        self.Sock    = Sock
        self.TimeOut = aTimeOut

    def _Parse(self, aConn, aAddr):
        R = {}

        hFile = aConn.makefile('rb', 0)
        Head  = GetHttpHead(hFile)
        if (Head):
            R['address'] = aAddr[0]

            Arr   = Head.get('head').split(' ')
            if (len(Arr) >= 2):
                R['command'] = Arr[0]
                R['path']    = Arr[1]

            Len = int(Head.get('content-length', '0'))
            #print('---_Parse', Head, 'Len', PostLen)
            if (Len > 0):
                Data = CallTry(3, aConn.recv, [Len])
                if (Data):
                    R['content'] = Data.decode("utf-8")
        return R

    def Run(self):
        self.Active = True
        while self.Active:
            try:
                Conn, Addr = self.Sock.accept()
            except OSError:
                self.DoTimeout()
                continue

            if (self.TimeOut >= 0):
                Conn.settimeout(self.TimeOut + 0.0)

            Request = self._Parse(Conn, Addr)
            if (Request):
                Responce = self.DoGet(Request)
                try:
                    Conn.send(Responce)
                except Exception as e:
                    self.DoTimeout()
                    print('Run()', e)
            Conn.close()

        self.Sock.close()

    def Stop(self):
        self.Active = False
