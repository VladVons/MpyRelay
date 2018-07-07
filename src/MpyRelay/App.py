'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.06.04
License:     GNU, see LICENSE for more details
Description: 
'''

import json
import time
import machine
#
from Conf          import Conf
from Log           import Log
from NetHttpServer import THttpServer
from NetHttpHead   import THeader
from Timer         import TTimer
import Net
import Pin
import Api
#

class TimerEx(TTimer):
    WatchHostErr = 0

    def DoTimeOut(self):
        if (self.Cnt > 0 and self.Cnt % 10 == 0):
            try:
                import _sys_unget
                _sys_unget.Api({})
            except Exception as E:
                print('DoTimeOut', E)

        cFL = Conf.Get('FlashLed')
        if (cFL):
            Pin.SetPinInv(cFL)

        cWH = Conf.Get('WatchHost')
        if (cWH):
            if (Net.SendData(cWH, 80)):
                self.WatchHostErr = 0
            else:
                self.WatchHostErr += 1
                if (self.WatchHostErr >= Conf.Get('WatchHostErr', 30)): 
                    Log.Print(1, self.__class__.__name__, 'OnTimer()', 'WatchHost reboot...')
                    time.sleep(5)
                    machine.reset()


class TApp(THttpServer):
    def __init__(self):
        self.Timer = TimerEx(Conf.Get('Timer', 2000))

    def DoTimeout(self):
        self.Timer.Handle()

    def DoGet(self, aRequest):
        Header = THeader()

        R    = None 
        Code = 200
        Content = aRequest.get('content', '{}')

        Path = aRequest.get('path')
        Func = Api.Load(Path)
        if (Func):
            try:
                Content = json.loads(Content)
                try:
                    R = Func(Content)
                    if (R is None):
                        R = {}
                    R = json.dumps(R)
                except Exception as e:
                    Code = 400
                    R = Log.Print(1, self.__class__.__name__, 'DoGet()', e)
            except:
                Code = 400
                R = Log.Print(1, self.__class__.__name__, 'DoGet()', 'json error %s' % Content)
        else:
            Code = 404
            R = 'Error: %s %s' % (Header.Codes.get(Code), Path)

        self.Timer.Init()
        print('In:', Path, Content, 'Out:', R)

        Header.AddCode(Code)
        Header.AddData(R)
        return str(Header)
