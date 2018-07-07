'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     17.04.17
License:     GNU, see LICENSE for more details
Description: 
'''

import time


#def SetTime():
#   try:
#        from  ntptime import settime.
#        settime()
#    except: pass


def GetTicks():
    return time.ticks_ms()


class TTimer:
    def __init__(self, aTimeOut = 1000):
        self.TimeOut = aTimeOut
        self.Handler = None
        self.Init()

    def Init(self):
        self.LastUpd = GetTicks()
        self.Cnt = 0

    def IsTimeOut(self):
        return GetTicks() - self.LastUpd > self.TimeOut

    def Handle(self):
        if (self.IsTimeOut()):
            self.Cnt += 1
            self.LastUpd = GetTicks()

            self.DoTimeOut()
            if (self.Handler):
                self.Handler()

    def DoTimeOut(self):
        pass
