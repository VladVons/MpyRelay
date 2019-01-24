#!/usr/bin/env python
# VladVons@gmail.com 

import sys
import socket
import urllib2 as urllib
import json


class TRelayScan():
    def __init__(self, aNet = None):
        if (aNet is None):
            aNet = self.GetLocalIP()
        self.Net = aNet.rsplit('.', 1)[0]

        self.IpBegin = 1
        self.IpEnd   = 255
        self.Port    = 80
        self.TimeOut = 0.3

    @staticmethod
    def GetLocalIP():
        Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            Socket.connect(('10.255.255.255', 0))
            Result = Socket.getsockname()[0]
        except:
            Result = '127.0.0.1'
        finally:
            Socket.close()
        return Result

    @staticmethod
    def GetUrl(aUrl, aData = {}):
        Request  = urllib.Request(aUrl)
        Request.add_header('Content-Type', 'text/json')
        try:
            Response = urllib.urlopen(Request, json.dumps(aData), timeout = 3)
            Data   = Response.read()
            Result = json.loads(Data)
        except:
            Result = {}
        return Result

    @staticmethod
    def IsUp_1(aAddr, aPort = 80, aTimeOut = 0.2):
        Socket = socket.socket()
        Socket.settimeout(aTimeOut)
        Result = Socket.connect_ex((aAddr, aPort))
        Socket.close()
        return Result == 0

    @staticmethod
    def IsUp_2(aAddr, aPort = 80, aTimeOut = 0.2):
        try:
            Socket = socket.create_connection((aAddr, aPort), timeout=aTimeOut)
            Socket.close()
            Result = True
        except:
            Result = False
        return Result

    def Scan(self):
        Result = []
        for ip in range(self.IpBegin, self.IpEnd):
            Addr = self.Net + '.' + str(ip)
            if self.IsUp_1(Addr, self.Port, self.TimeOut):
                Data = self.GetUrl('http://%s:%s' % (Addr, self.Port))
                if (Data):
                    Str = 'IP: %s, MAC: %s, ID: %s, Uptime: %s' % (Addr, Data['MAC'], Data['ID'], Data['Uptime'])
                    print(Str)
                    Result.append(Str)
                else:
                    print(Addr, self.Port, '?')
            else:
                if (ip % 10 == 0):
                    #sys.stdout.write('.')
                    #sys.stdout.flush()
                    #print('.\b')
                    print(Addr, self.Port)
        return Result


#RelayScan = TRelayScan('192.168.2.0')
RelayScan = TRelayScan()
#RelayScan.IpBegin = 130
#RelayScan.IpEnd   = 140

Items = RelayScan.Scan()
print('Summory')
Cnt = 0
for Item in Items:
    Cnt += 1
    print(Cnt, Item) 
