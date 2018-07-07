'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.06.17
License:     GNU, see LICENSE for more details
Description:.
'''

import Pin


def Api(aData):
    R = {}
    for Key in aData.get('pin', []):
        R[Key] = Pin.GetPin(int(Key))
    return R
