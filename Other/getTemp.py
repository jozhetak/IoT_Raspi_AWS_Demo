#!/usr/bin/python
import time
import wiringpi2
import os
import struct
from time import sleep

""" Temperature Humidity Setting """
wiringpi2.wiringPiSetup()
i2c = wiringpi2.I2C()
dev = i2c.setup(0x40)

i2c.writeReg16(dev,0x02,0x10)
i2c.writeReg8(dev,0x00,0x00)
sleep((6350.0 + 6500.0 +  500.0)/1000000.0)
tmpVal = ((struct.unpack('4B', os.read(dev,4)))[0] << 8 | (struct.unpack('4B', os.read(dev,4)))[1])
os.close(dev)
print round(((tmpVal / 65535.0) * 165 - 40), 2)
