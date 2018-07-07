'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2017.02.04
License:     GNU, see LICENSE for more details
Description: 
'''

import network
import time
import ubinascii
import sys
#
from Log import Log


def GetMac(aObj):
    MacBin = aObj.config('mac')
    return ubinascii.hexlify(MacBin).decode('utf-8')

def SetAP(aESSID, aPassw):
    Obj  = network.WLAN(network.AP_IF)
    Obj.active(False)
    #MacHex = GetMac(Obj)
    #ESSID  = '%s-%s' % (aESSID, MacHex[-4:])
    #Obj.config(essid=ESSID, authmode=network.AUTH_WPA_WPA2_PSK, password=aPassw)
    #print('ESSID:', ESSID, 'Passw-8:', aPassw)
    #print('Network', Obj.ifconfig())

def TryConnect(aObj, aCnt):
    while (not aObj.isconnected()) and (aCnt > 0):
        sys.stdout.write('.')
        time.sleep_ms(250)
        aCnt -= 1
    return aCnt

def Connect(aESSID, aPassw):
    print('Connecting SSID %s, password %s' % (aESSID, aPassw))

    Obj = network.WLAN(network.STA_IF)
    if (TryConnect(Obj, 20) == 0):
        Obj.active(True)
        Obj.connect(aESSID, aPassw)
        TryConnect(Obj, 20)
    print('Network', Obj.ifconfig())
    print('MAC:', GetMac(Obj))
