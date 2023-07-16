'''Reset the oled and pico led'''
from machine import Pin, Timer, I2C
import sh1106

i2c_data = 16
i2c_clock = 17

# pico led is on pin 25, set it to low to turn it off
led = Pin(25, Pin.OUT)
led.low()

# i2c connection to oled, connect to the display
i2c = machine.I2C(0, scl=machine.Pin(i2c_clock), sda=machine.Pin(i2c_data), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3c)

# clear the display
display.fill(0)
display.show()