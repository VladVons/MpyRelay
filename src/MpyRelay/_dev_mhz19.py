'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.04.25
License:     GNU, see LICENSE for more details
Description:
'''

import os
#
from Serial import TSerial


class TMHZ19(TSerial):
    def IsCheckSum(self, aData):
        Sum = 0
        for i in range(1, 7):
            Sum += aData[i]
        Sum = ~Sum & 0xFF
        Sum += 1

        CheckSum = aData[-1]
        return (CheckSum == Sum)

    def GetCO2(self):
        Out = b'\xff\x01\x86\x00\x00\x00\x00\x00\x79'
        try:
            In = self.Send(Out, 9) 
            R = (In[2] * 256) + In[3]
        except:
            R = None
        return R


def Api(aData):
    aPort  = aData.get('port', 1)
    MHZ19  = TMHZ19(aPort, 9600)
    R = MHZ19.GetCO2()
    return {'co2': R}
