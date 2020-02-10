'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2020.02.10
License:     GNU, see LICENSE for more details
Description: micropython ESP8266
             BME temperature-humidity-preasure sensor
'''

import machine
#
from Lib_dev_bme280 import BME280
from Log import Log


def Api(aData):
    i2c = machine.I2C(scl= machine.Pin(5),sda= machine.Pin(4), freq=10000)
    try:
        bme = BME280(i2c=i2c)
        t, p, h = bme.read_compensated_data()
        R = [t, h, p]
    except Exception as e:
        Log.Print(1, 'Err: DevBME280', 'Api()', e)
        R = [None, None, None]
    return {'temperature': R[0], 'humidity': R[1], 'preasure': R[2]}
