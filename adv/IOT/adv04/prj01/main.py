#########################匯入模組#########################
from machine import Pin, ADC, PWM
from time import sleep
import adv10.mcu as mcu

#########################函式與類別定義#########################


#########################宣告與設定#########################
gpio = mcu.gpio()
light_sensor = ADC(0)
frequency = 1000
duty_cycle = 0
duty_c = 0
RED = PWM(Pin(gpio.D5), freq=frequency, duty=duty_cycle)
GREEN = PWM(Pin(gpio.D6), freq=frequency, duty=duty_cycle)
BLUE = PWM(Pin(gpio.D7), freq=frequency, duty=duty_cycle)
#########################主程式#########################
while True:
    light_sensor_reading = light_sensor.read()

    # sleep(0.2)
    if light_sensor_reading < 400:
        light_sensor_reading = 0

    RED.duty(light_sensor_reading)
    BLUE.duty(light_sensor_reading)
    GREEN.duty(light_sensor_reading)

    # light_sensor_reading = light_sensor.read()
    print(f"value{light_sensor_reading}, {round(light_sensor_reading * 100 / 1024)}%")
    # sleep(1)
