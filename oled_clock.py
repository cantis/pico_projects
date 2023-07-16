'''Show the date and time on OLED display'''

from machine import Pin, Timer, I2C
import utime
import time
import sh1106

i2c_data = 16
i2c_clock = 17
tim = Timer()
led = Pin(25, Pin.OUT)

i2c = machine.I2C(0, scl=machine.Pin(i2c_clock), sda=machine.Pin(i2c_data), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3c)

def tick(timer):
    global led
    global display
    led.toggle()
    now = time.localtime()
    date_str = "Date: {}/{:02d}/{:02d}".format(now[0], now[1], now[2])
    time_str = "Time: {:02d}:{:02d}:{:02d}".format(now[3], now[4], now[5])

    display.fill(0)
    # this .text is from the FrameBuffer `FrameBuffer.text(s, x, y[, c])`
    # the font for the text is always 8x8 so you move down the Y co-ord by 9 or so for a new line
    display.text(date_str,0,0,1)
    display.text(time_str,0,9,1)
    display.show()

tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)