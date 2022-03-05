import machine
import mpu6050

# Create i2c object
i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16))
mpu = mpu6050.accel(i2c=i2c)
tim = machine.Timer()

mpu.begin(

def tick(tim):
    global mpu
    print(mpu.get_values())
    
tim.init(freq=2, mode=machine.Timer.PERIODIC, callback=tick)

