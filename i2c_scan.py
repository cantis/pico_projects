""" Scan i2c bus 0 for attached devices, return any id's found """
# EYoung 21 Feb 2022, updated July 2023
# Change the pins to match your setup!

from machine import I2C
i2c_clock = 17 # Clock
i2c_data = 16 # Data

# Set up an i2c connection on pins 16 and 17
i2c = machine.I2C(0, scl=machine.Pin(i2c_clock), sda=machine.Pin(i2c_data))

# Run the scan of that i2c buss, returns a list
devices = i2c.scan()

# Print out what we found
if devices:
    print('Found Devices:')
    for d in devices:
        print(f'hex: {hex(d)}  dec:{d}')
else:
    print('No Devices Found')