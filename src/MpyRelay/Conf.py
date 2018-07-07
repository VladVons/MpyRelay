'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.06.10
License:     GNU, see LICENSE for more details
Description:.
'''


class TConf():
    def __init__(self, aModule = 'AppConf'):
        self.Name = aModule
        self.Obj  = __import__(aModule)

    def Get(self, aKey, aDef = None):
        try:
            R = getattr(self.Obj, aKey)
        except:
            R = aDef
        return R


class TConfInit(TConf):
    def Write(self, aKey, aValue, aChar):
        with open(self.Name + '.py', "a") as File:
            Data = '%s = %s%s%s\n' % (aKey, aChar, aValue, aChar)
            File.write(Data)

    def Init(self, aForce = False):
        Changed = False
        for Key in dir(self.Obj):
            if (not '__' in Key):
                Value = self.Get(Key)
                Type  = type(Value)
                if (aForce) or (Value is None) or (Type is str and Value == ''):
                    Value = input('`%s` (default %s) >' % (Key, Value))
                    if (Value):
                        Changed = True
                        Bracket = '"' if (Type is str) else ''
                        self.Write(Key, Value, Bracket)
        return Changed


Conf = TConf()
