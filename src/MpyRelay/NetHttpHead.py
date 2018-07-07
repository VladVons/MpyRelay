'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2108.06.03
License:     GNU, see LICENSE for more details
Description: 
'''

import time
#
from Lib import CallTry


def GetHttpHead(aSock):
    R = {}

    while True:
        # see makefile()
        Line = CallTry(3, aSock.readline, [])
        #print(Line)

        if (not Line) or (Line == b'\r\n'):
            break

        Line = Line.decode("utf-8")
        Arr = Line.split(':')
        if (len(Arr) == 1):
            Key   = 'head'
            Value = Arr[0]
        else:
            Key   = Arr[0]
            Value = Arr[1]
        R[Key.lower()] = Value.strip()
    return R


class THeader(list):
    Codes = {
        200: 'OK',
        400: 'Bad Request',
        404: 'Not Found'
    }

    def __str__(self):
        return '\r\n'.join(self)

    def AddCode(self, aCode):
        Data = 'HTTP/1.1 %d %s' % (aCode, self.Codes.get(aCode))
        self.append(Data)
        #self.append('Content-Type: text/html')
        self.append('Content-Type: text/json')

    def AddData(self, aData):
        self.append('Content-Length: %d' % len(aData))
        self.append('')
        self.append(aData)
