'''
Author:      Vladimir Vons <VladVons@gmail.com>
Created:     2019.05.15
License:     GNU, see LICENSE for more details
Description: micropython ESP8266
             MQ2 methan gas sensor
https://github.com/kartun83/micropython-MQ
'''

from Lib_dev_mq  import BaseMQ
#
from Log import Log


class TMQ2(BaseMQ):
    ## Clean air coefficient
    MQ2_RO_BASE = float(9.83)

    def __init__(self, pinData, pinHeater=-1, boardResistance = 10, baseVoltage = 5.0, measuringStrategy = BaseMQ.STRATEGY_ACCURATE):
        # Call superclass to fill attributes
        super().__init__(pinData, pinHeater, boardResistance, baseVoltage, measuringStrategy)
        pass

    ## Measure liquefied hydrocarbon gas, LPG
    def readLPG(self):
        return self.readScaled(-0.45, 2.95)
        
    ## Measure methane  
    def readMethane(self):
        return self.readScaled(-0.38, 3.21)

    ## Measure smoke
    def readSmoke(self):
        return self.readScaled(-0.42, 3.54)

    ## Measure hydrogen
    def readHydrogen(self):
        return self.readScaled(-0.48, 3.32)

    ##  Base RO differs for every sensor family
    def getRoInCleanAir(self):
        return self.MQ2_RO_BASE


def Get(aPin = 0):
    try:
        MQ2 = TMQ2(pinData = aPin, baseVoltage = 3.3)
        print("Calibrating")
        MQ2.calibrate()

        print("smoke")
        S = MQ2.readSmoke()
        print("lpg")
        L = MQ2.readLPG()
        print("methane")
        M = MQ2.readMethane()
        print("hydrogen")
        H = MQ2.readHydrogen()
        R = [S , L, M, H]
    except Exception as e:
        Log.Print(1, 'dev_mq2', 'Get()', e)
        R = [None, None, None, None]
    return R


def Api(aData):
    aPin = aData.get('pin', 0)
    R    = Get(aPin)
    return {'smoke': R[0], 'lpg': R[1], 'methane': R[2], 'hydrogen': R[3]}
