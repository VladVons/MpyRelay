'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2017.02.01
License:     GNU, see LICENSE for more details
Description: 
'''

import time
import os
#
from Conf import Conf


class TEcho():
    def Write(self, aMsg):
        pass

    
class TConsole(TEcho):
    def Write(self, aMsg):
        print(aMsg)

'''
class TFile(TEcho):
    def __init__(self, aName):
        self.MaxSize = 10000
        self.Name    = aName

    def Write(self, aMsg):
        try:
            Len = os.stat(self.Name)[6]
            if (Len > self.MaxSize):
                os.remove(self.Name)
        except: pass

        with open(self.Name, 'a') as hFile:
            hFile.write(aMsg + '\n')
'''

'''
class THost(TEcho):
    def __init__(self, aHost, aPort):
        self.Host = aHost
        self.Port = aPort

    def Write(self, aMsg):
        from Net import SendData
        SendData(self.Host, self.Port, bytearray(aMsg))
'''

class TLog():
    def __init__(self):
        self.Level  = 1
        self.Cnt    = 0
        self.Echoes = [] 

    def AddEcho(self, aEcho):
        self.Echoes.append(aEcho) 

    def Print(self, aLevel, *aParam):
        R = ''
        if (aLevel <= self.Level):
            self.Cnt += 1
            R = '%d,%d,%d,%s,%s%s' % (time.time(), self.Cnt, aLevel, Conf.Get('ID'), ' ' * aLevel, list(aParam))
            for Echo in self.Echoes: 
                Echo.Write(R)
        return R


Log = TLog()
Log.AddEcho(TConsole())
#Log.AddEcho(TFile('App.log'))

'''
cDH = Conf.Get('DebugHost')
if (cDH):
    Host, Port = cDH.split(':')
    Log.AddEcho(THost(Host, int(Port)))
'''

#Log.Print(1, 'Hello')
