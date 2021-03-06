#!/usr/bin/python
import time
from notsmb import notSMB

""" CO2 Setting """
I2CBUS = 1
CO2_ADDR = 0x68
READ = 0x22
readBytes = [0x00, 0x08, 0x2A]
bus = notSMB(I2CBUS)

while True:
    try:
        resp = bus.i2c(CO2_ADDR,[0x22,0x00,0x08,0x2A],4)
        time.sleep(0.1)
        co2Val = (resp[1]*256) + resp[2]
        
        if co2Val < 8000:
          break
    except:
        blank =0;

print co2Val
