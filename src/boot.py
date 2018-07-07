'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     04.02.17
License:     GNU, see LICENSE for more details
Description: micropython ESP8266

https://forum.micropython.org/viewtopic.php?f=2&t=4868&p=28008#p28008
'''

import gc
import micropython
import sys
import os, machine

# enable print() in daily builds
#try:
#    os.dupterm(machine.UART(0, 115200), 1)
#except: pass

print('boot.py')

micropython.alloc_emergency_exception_buf(100)

#import esp
#esp.osdebug(None)
#esp.osdebug(0) 

#import webrepl_setup
#https://micropython.org/webrepl/?
#import webrepl
#webrepl.start()


gc.collect()
#micropython.mem_info()
print('mem_free', gc.mem_free())

#print(sys.version, sys.platform)
print(os.uname())
