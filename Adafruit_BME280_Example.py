from Adafruit_BME280 import *
from time import sleep
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

degrees = sensor.read_temperature()
pascals = sensor.read_pressure()
hectopascals = pascals / 100
#humidity = sensor.read_humidity()

degrees = sensor.read_temperature()
pascals = sensor.read_pressure()
hectopascals = pascals / 100

cur_floor = hectopascals
prev_floor = hectopascals

while True:
    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    sleep(2)
    cur_floor = hectopascals

    if((cur_floor - prev_floor) > 0.36):
        print 'down'
        print ('prev = ', prev_floor)
        print ('cur = ', cur_floor)
        print ('cur-prev = ',cur_floor-prev_floor)
        prev_floor = cur_floor
    elif((cur_floor - prev_floor) < -0.36):
        print 'up'
        print('prev = ', prev_floor)
        print('cur = ', cur_floor)
        print('cur-prev = ',cur_floor-prev_floor)
        prev_floor = cur_floor


