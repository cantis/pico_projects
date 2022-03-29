from machine import Pin
from time import sleep

led1 = Pin(27, Pin.OUT)
led2 = Pin(25, Pin.OUT)
led1.value(1)
sleep(1)
led2.value(1)
sleep(4)
led1.value(0)
sleep(1)
led2.value(0)
