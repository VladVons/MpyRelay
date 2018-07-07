'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.07.02
License:     GNU, see LICENSE for more details
Description:.
'''

import os


def Filter(aMask):
    R = []

    Path, XXX = aMask.rsplit('*', 1)
    Dir, Mask = Path.rsplit('/', 1)
    for File in os.listdir(Dir):
        if (File.startswith(Mask)):
            R.append(Dir + '/' + File)
    return R


def TryDel(aFile, aErr):
    try:
        os.remove(aFile)
    except:
        aErr.append(aFile)


def Del(aFiles):
    R = []
    for Item in aFiles:
        if ('*' in Item):
            for File in Filter(Item):
                TryDel(File, R)
        else:
            TryDel(Item, R)
    return R


def Api(aData):
    aFiles = aData.get('files', [])
    return {'error': Del(aFiles)}
