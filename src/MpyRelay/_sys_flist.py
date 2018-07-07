'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.07.02
License:     GNU, see LICENSE for more details
Description:.
'''

import os


def Api(aData):
    aDir = aData.get('dir', '')
    return {'files': os.listdir(aDir)}
