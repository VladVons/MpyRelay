'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.06.15
License:     GNU, see LICENSE for more details
Description:.
'''

#import sys
#import gc
import time

'''
def DelModule(aMod):
    try:
        Name = aMod.__name__
        del(aMod)
        del(sys.modules[Name])
        gc.collect()
    except:
        print('Error', Name)
'''


def CallTry(aCnt, aFunc, aArgs):
    R = None
    Sleep = 0
    while (aCnt > 0):
        aCnt -= 1
        try:
            R = aFunc(*aArgs)
            break
        except Exception as E:
            Sleep += 0.1
            time.sleep(Sleep)
            print('CallTry', aArgs, aCnt, E)
    return R
