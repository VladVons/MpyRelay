'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.06.17
License:     GNU, see LICENSE for more details
Description:.
'''

import Pin


def Api(aData):
    for Key in aData:
        Pin.SetPin(int(Key), int(aData[Key]))
