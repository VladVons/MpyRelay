'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2017.04.17
License:     GNU, see LICENSE for more details
Description: 
'''

from machine import Pin


def SetPin(aPin, aValue):
    Obj = Pin(aPin, Pin.OUT)
    Obj.value(aValue)
    return Obj.value()

def SetPinInv(aPin):
    Obj = Pin(aPin, Pin.OUT)
    Obj.value(not Obj.value())
    return Obj.value()

def GetPin(aPin):
    try:
        Obj = Pin(aPin, Pin.OUT)
        R = Obj.value()
    except:
        R = -1
    return R
