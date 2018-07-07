'''
Copyright:   (c) 2017, Vladimir Vons, UA
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.04.25
License:     GNU, see LICENSE for more details
'''

from Serial import TSerial


class TPzem_004(TSerial):
    def IsCheckSum(self, aData):
        List     = list(aData)
        CheckSum = List[-1]
        List.pop()
        Sum = sum(List)
        return (CheckSum == Sum % 256)

    def IsReady(self):
        Out = b'\xB4\xC0\xA8\x01\x01\x00\x1E'
        In  = self.Send(Out, 7)
        return In != None

    def GetVoltage(self):
        Out = b'\xB0\xC0\xA8\x01\x01\x00\x1A'
        In  = self.Send(Out, 7)
        return In[2] + (In[3] / 10.0) 

    def GetCurrent(self):
        Out = b'\xB1\xC0\xA8\x01\x01\x00\x1B'
        In  = self.Send(Out, 7)
        return In[2] + (In[3] / 100.0)

    def GetPower(self):
        Out = b'\xB2\xC0\xA8\x01\x01\x00\x1C'
        In  = self.Send(Out, 7)
        return (In[1] * 256) + In[2]

    def GetRegPower(self):
        Out = b'\xB3\xC0\xA8\x01\x01\x00\x1D'
        In  = self.Send(Out, 7)
        return (In[1] * 256 * 256) + (In[2] * 256) + In[3]


def Api(aData):
    R = {}

    aPort  = aData.get('port', 2)
    aValue = aData.get('value', ['Voltage'])
    Pzem = TPzem_004(aPort, 9600)
    if (Pzem.IsReady()):
        for Value in aValue:
            try:
                Func = getattr(Pzem, 'Get%s' % Value)
                R[Value] = Func()
            except: pass
    return R
