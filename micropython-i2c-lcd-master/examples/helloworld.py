import i2c_lcd
from machine import I2C

i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16)) 
d = i2c_lcd.Display(i2c)

d.home()
d.write('Hello World')
