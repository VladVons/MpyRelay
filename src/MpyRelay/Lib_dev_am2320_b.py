# https://github.com/alexmrqt/Adafruit_CircuitPython_am2320.git


import struct
import time
from micropython import const


_AM2320_DEFAULT_ADDR = const(0x5C)
_AM2320_CMD_READREG = const(0x03)
_AM2320_REG_TEMP_H = const(0x02)
_AM2320_REG_HUM_H = const(0x00)


def _crc16(data):
    crc = 0xffff
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc


class AM2320:
    """A driver for the AM2320 temperature and humidity sensor.
    :param i2c_bus: The `I2C` object to use. This is the only required parameter.
    :param int address: (optional) The I2C address of the device.
    """
    def __init__(self, i2c_bus, address=_AM2320_DEFAULT_ADDR):
        self._i2c_bus = i2c_bus
        self._addr = address
        print('---1a', i2c_bus, address)

    def _read_register(self, register, length):
        # wake up sensor
        print('---1')
        time.sleep(0.01)  # wait 10 ms

        try:
            self._i2c_bus.writeto(self._addr, bytes([0x00]))
        except OSError:
            print('---err')

        time.sleep(0.01)  # wait 10 ms

        # Send command to read register
        cmd = [_AM2320_CMD_READREG, register & 0xFF, length]
        # print("cmd: %s" % [hex(i) for i in cmd])
        print('---2')
        self._i2c_bus.writeto(self._addr, bytes(cmd))
        time.sleep(0.002)  # wait 2 ms for reply
        result = bytearray(length+4) # 2 bytes pre, 2 bytes crc
        print('---3')
        self._i2c_bus.readfrom_into(self._addr, result)
        print('---4')
        # print("$%02X => %s" % (register, [hex(i) for i in result]))
        # Check preamble indicates correct readings
        if result[0] != 0x3 or result[1] != length:
            raise RuntimeError('I2C modbus read failure')
        # Check CRC on all but last 2 bytes
        crc1 = struct.unpack("<H", bytes(result[-2:]))[0]
        crc2 = _crc16(result[0:-2])
        if crc1 != crc2:
            raise RuntimeError('CRC failure 0x%04X vs 0x%04X' % (crc1, crc2))
        return result[2:-2]

    @property
    def temperature(self):
        """The measured temperature in celsius."""
        temperature = struct.unpack(">H", self._read_register(_AM2320_REG_TEMP_H, 2))[0]
        if temperature >= 32768:
            temperature = 32768 - temperature
        return temperature/10.0

    @property
    def relative_humidity(self):
        """The measured relative humidity in percent."""
        humidity = struct.unpack(">H", self._read_register(_AM2320_REG_HUM_H, 2))[0]
        return humidity/10.0
