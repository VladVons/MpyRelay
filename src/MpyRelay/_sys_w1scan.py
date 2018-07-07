'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.07.02
License:     GNU, see LICENSE for more details
Description: micropython ESP8266
             DHT22 temperature-humidity sensor
'''

import machine
import onewire
import ubinascii


def Get(aPin):
    Pin = machine.Pin(aPin)
    W1  = onewire.OneWire(Pin)

    R = []
    Devs = W1.scan()
    if (Devs):
        for Dev in Devs:
            Hex = ubinascii.hexlify(Dev).decode('utf-8')
            R.append(Hex)
    return R


def Api(aData):
    aPin = aData.get('pin', 0)
    R = Get(aPin)
    return {'scan': R}
