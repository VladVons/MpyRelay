'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.06.17
License:     GNU, see LICENSE for more details
Description:.
'''

from Log import Log


def Api(aData):
    Msg   = aData.get('msg')
    Level = aData.get('level', 1)
    R = Log.Print(Level, Msg)
    return {'result': R}
