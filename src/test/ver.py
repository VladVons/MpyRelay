#!/usr/bin/env python3

import os
import json

def Export(aFile):
    Ver   = '1.0.11'
    Size  = 0
    Names = []

    Dir  = '.'
    for Root, Subdirs, Files in os.walk(Dir):
        #print('root', Root)
        #print('subdir', Subdirs)
        Files.sort()
        for File in Files:
            if (File.startswith('ver.') or File.startswith('.')):
                #print('Skip', File)
                continue

            Name = '%s/%s' % (Root, File)
            Names.append(Name[2:])

            Len = int(os.stat(Name)[6])
            Size += Len

            print(Len, Name)

    Data = {"Ver": Ver, "Size": Size, "Files": Names}
    print('Files', len(Names), 'Size', Size)

    with open(aFile, 'w') as hFile:
        json.dump(Data, hFile)

Export('ver.json')
