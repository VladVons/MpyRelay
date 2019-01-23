#!/usr/bin/env python

import sys
import socket
import urllib2 as urllib
import json


def GetLocalIP():
    Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        Socket.connect(('10.255.255.255', 0))
        Result = Socket.getsockname()[0]
    # ToDo type
    except:
        Result = '127.0.0.1'
    finally:
        Socket.close()
    return Result


def GetData(aUrl, aData = {}):
    Request  = urllib.Request(aUrl)
    Request.add_header('Content-Type', 'text/json')
    try:
        Response = urllib.urlopen(Request, json.dumps(aData), timeout = 3)
        Data   = Response.read()
        Result = json.loads(Data)
    except:
        Result = {}
    return Result

def IsUp(aAddr, aPort = 80):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.2)
    Result = sock.connect_ex((aAddr, aPort))
    sock.close()
    return Result == 0

def Run(aNet = '', aPort = 80, Range = [0, 255]):
    if (aNet == ''):
         aNet = GetLocalIP()

    Result = []
    for ip in range(*Range):
        Addr = aNet + str(ip)
        if IsUp(Addr, aPort):
            Data = GetData('http://%s:%s' % (Addr, aPort))
            if (Data):
                Str = 'IP: %s, MAC: %s, ID: %s, Uptime: %s' % (Addr, Data['MAC'], Data['ID'], Data['Uptime'])
                print(Str)
                Result.append(Str)
            else:
                print(Addr, '?')
        else:
            #sys.stdout.write('.')
            #sys.stdout.flush()
            #print('.\b')
            print(Addr)

    for Item in Result:
        print(Item) 

print('192.168.2.1'.split('.'))
#Run('192.168.2.0', 80, [120,140])
#print(IsUp('192.168.2.132', 80))
#print(IsUp('192.168.2.162', 80))

#print(socket.gethostbyname(socket.gethostname()))
#print(socket.gethostbyname(socket.getfqdn()))
#GetIp4Address()
print(GetLocalIP())