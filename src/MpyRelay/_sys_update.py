'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.06.14
License:     GNU, see LICENSE for more details
Description: 
'''

import json
import os
import gc
#
from Conf import Conf
from Log  import Log
from NetHttpHead import GetHttpHead
from NetUrl      import LoadToStr, LoadToStream


def Update(aUrl):
    Data = LoadToStr(aUrl)
    print('aUrl', aUrl, 'Data', Data)
    try:
        Data = json.loads(Data)
    except Exception as e:
        print('Update', e)
        return False

    Size1 = Data.get('Size', 0)
    Size2 = 0

    Root  = aUrl.rsplit('/', 1)[0]
    Files = Data.get('Files', [])
    for File in Files:
        gc.collect()

        Arr = File.rsplit('/', 1)
        if (len(Arr) == 2):
            try:
                os.mkdir(Arr[0])
            except: pass

        Url = Root + '/' + File
        with open(File, "w") as hFile:
            Len = LoadToStream(Url, 80, hFile)
            if (Len):
                Size2 += Len

            print('Size %s/%s' % (Size1, Size2), 'Len', Len, 'Url', Url)
    return Size1 == Size2


def Api(aData):
    gc.collect()

    Url = aData.get('url')
    R = Update(Url)
    Log.Print(1, 'Api', 'Update()', R)
    return {'result': R, 'ID': Conf.Get('ID'), 'hint': 'Reset ?'}
