'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2018.07.02
License:     GNU, see LICENSE for more details
Description:.
'''

import os


def Api(aData):
    R = []
    for File in os.listdir('/MpyRelay'): 
        if (File.startswith('_')) and (File != '__init__'):
            Name = File.replace('_', '/').replace('.py', '')
            R.append(Name)
    return {'api': R}
