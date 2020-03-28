'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2020.02.24
License:     GNU, see LICENSE for more details
Description: micropython ESP8266
             DHT21 temperature-humidity sensor
'''

import machine
import time
import dht
#
from Log import Log


def Get(aPin):
    #Pin = machine.Pin(aPin, machine.Pin.IN, machine.Pin.PULL_UP)
    Pin = machine.Pin(aPin)
    Obj = dht.DHT11(Pin)

    try:
        time.sleep_ms(250)
        Obj.measure()
        time.sleep_ms(250)
        T = Obj.temperature()
        H = Obj.humidity()
        R = [T, H]
    except Exception as e:
        Log.Print(1, 'Err: DevDHT11', 'Get()', e)
        R = [None, None]
    return R


def Api(aData):
    aPin = aData.get('pin', 0)
    R = Get(aPin)
    return {'temperature': R[0], 'humidity': R[1]}
