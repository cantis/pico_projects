# oled_helloworld.py Evan Young March 2022

import machine
import utime
import sh1106

# This is for a 1.3in oled I purchased from Amazon
# https://www.amazon.ca/gp/product/B085RYPHT2/ref=ppx_yo_dt_b_asin_title_o02_s01?ie=UTF8&psc=1

#The library for sh1106 is available at
# https://github.com/robert-hh/SH1106

# Set up an i2c connection on pins 16 and 17
i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16), freq=400000)
# Create a display instance
display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3c)

# blank the screen
display.fill(0)
# write the text I wanted
display.text("Hello World",0 ,0 ,1)
# and show it
display.show()


