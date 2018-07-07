'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.06.17
License:     GNU, see LICENSE for more details
Description:.
'''

def Api(aData):
    Msg = aData.get('msg')
    print(Msg)
    return {'result': Msg}
