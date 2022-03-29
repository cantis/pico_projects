""" Scan i2c bus 0 (16,17) for attached devices, return any id's found """
# EYoung 21 Feb 22
# Change the pins to match your setup! 

from machine import I2C

# Set up an i2c connection on pins 16 and 17
i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16)) 

# Run the scan of, returns a list
devices = i2c.scan()

# Print out what we found
if devices:
    for d in devices:
        print(hex(d)) 