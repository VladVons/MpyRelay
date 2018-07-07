'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.06.29
License:     GNU, see LICENSE for more details
Description:.
'''

from Log import Log


def Exec(aValue):
    #aValue = 'result = (2+3)*2'
    Vars   = {}
    try:
        exec(aValue, globals(), Vars)
        R = Vars.get('result')
    except Exception as e:
        Log.Print(0, 'Exec()', e)
        R = e
    return R


def Api(aData):
    Script = aData.get('script')
    return {'result' : Exec(Script)}
