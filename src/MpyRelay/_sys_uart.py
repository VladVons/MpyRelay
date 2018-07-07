'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.04.28
License:     GNU, see LICENSE for more details
Description:
'''

from Serial import TSerial


class TUart(TSerial):
    def IsCheckSum(self, aData):
        return True


def Api(aData):
    APort = aData.get('port', 1)
    AData = aData.get('data', '-hello-')
    ALen  = aData.get('len',  1)

    Uart   = TUart(APort, 9600)
    R = Uart.Send(AData, ALen)
    return {'result': R}
