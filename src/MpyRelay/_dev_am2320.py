'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2020.03.22
License:     GNU, see LICENSE for more details
Description: micropython ESP8266
             am2320 temperature-humidity sensor
'''

import machine
#
from Lib_dev_am2320 import AM2320
from Log import Log


def Api(aData):
    i2c = machine.I2C(scl= machine.Pin(5), sda= machine.Pin(4))
    try:
        Obj = AM2320(i2c)
        Obj.measure()
        R = [Obj.temperature(), Obj.humidity()]
    except Exception as e:
        Log.Print(1, 'Err: dev_am2320', 'Api()', e)
        R = [None, None]
    return {'temperature': R[0], 'humidity': R[1]}
