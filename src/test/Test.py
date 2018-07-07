class TC1():
    s1 = '123'

    def M1(self, aData):
        print(aData, self.s1)

    @staticmethod
    def M2(aData):
        print(aData, TC1.s1)
        TC1.M3(3)

    @staticmethod
    def M3(aData):
        print(aData)


#Res = Gpio_Read({'pin': [1,2,3]})
#print(Res)

#Data = {"A1":123, "R4": 345, "C2": 456}

#StrOut = '\xff\x01\x86\x00\x00\x00\x00\x00\x79'
#print('SttOut', StrOut)

#a1, a2, a3 = '1,2,3'.split(',', 2)
#print(a1, a2, a3)

#DebugHost='192.168.2.11:1'
#Host, Port = DebugHost.split(':', 1)
#print(Host, Port)


#Test = (1, 2)
#print(Test.b)


#File = '/Dir1/Api_*'
#Path, _ = File.rsplit('*', 1)
#print(Path)

#Arr = File.split('*')
#if (len(Arr) > 1):
#    Dir = Arr[0].rsplit('/', 1)
#    print('--1', Arr[0], Dir)
#print('--2', Arr)

print(1 % 10)
