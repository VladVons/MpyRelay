'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.06.17
License:     GNU, see LICENSE for more details
Description:.
'''

import os


def Tail(aFile, aOfst):
    R = ''
    try:
        Len = os.stat(aFile)[6]
        Ofst = max(0, Len - aOfst)
        with open(aFile, 'rt') as File:
            File.seek(Ofst)
            File.readline()
            for Line in File:
                R += Line
    except:
        R = 'not found %s' % aFile
    return R


def Api(aData):
    aFile = aData.get('file')
    aOfst = aData.get('ofst', 1000)
    R = Tail(aFile, aOfst)
    return {'result': R}
