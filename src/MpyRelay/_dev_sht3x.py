'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.02.11
License:     GNU, see LICENSE for more details
Description: micropython ESP8266
             SHT31 temperature-humidity sensor
'''

import machine
#
from Lib_dev_sht3x import SHT31
from Log import Log


def Api(aData):
    i2c = machine.I2C(scl= machine.Pin(5), sda= machine.Pin(4))
    try:
        Obj = SHT31(i2c)
        R = Obj.get_temp_humi()
    except Exception as e:
        Log.Print(1, 'Err: dev_sht3x', 'Api()', e)
        R = [None, None]
    return {'temperature': R[0], 'humidity': R[1]}
