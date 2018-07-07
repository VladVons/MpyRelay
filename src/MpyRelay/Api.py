'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.06.17
License:     GNU, see LICENSE for more details
Description:.
'''


def Test(aData):
    print('Test', aData)


Url = {
    '/':          '/index',
    '/sys/test':  Test
    }

def Load(aPath):
    R = Url.get(aPath, aPath)
    if (type(R).__name__ != 'function'):
        Mod = R.replace('/', '_')
        print('--1', aPath, Mod)
        try:
            R = getattr(__import__(Mod), 'Api')
        except:
            R = None
    return R
