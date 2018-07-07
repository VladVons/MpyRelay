'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2017.02.17
License:     GNU, see LICENSE for more details
Description: 
'''

import gc
import os
import time
import machine
#
import App
from   Log import Log
from   Conf import Conf

#from Lib import DelModule


def Configure():
    from Conf import TConfInit

    ConfInit = TConfInit()
    if (ConfInit.Init()):
        print('rebooting...')
        time.sleep(2)
        machine.reset()


def ConnectWan():
    import NetWLan

    print('ConnectWan...')

    NetWLan.SetAP(None, None)
    #print()

    ESSID  = Conf.Get('STA_ESSID')
    Paswd  = Conf.Get('STA_Password')
    NetWLan.Connect(ESSID, Paswd)

    #DelModule(NetWLan)
    print()


def Exec():
    Configure()
    ConnectWan()

    gc.collect()
    print('mem_free', gc.mem_free())

    #Log.AddEcho(THost('192.168.2.11', 8008))
    Log.Print(1, 'Run', 'Exec()', 'Start')

    App1 = App.TApp()
    App1.Connect(80, Conf.Get('SockTimeOut', 0.1))
    #try:
    App1.Run()
    #except Exception as e:
    #    Log.Print(1, 'Run', 'Exec()', 'Reboot...', e)
    #    time.sleep(10)
    #    machine.reset()
