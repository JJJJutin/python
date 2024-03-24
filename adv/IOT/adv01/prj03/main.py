#########################匯入模組#########################
from machine import Pin, PWM
from time import sleep

#########################函式與類別定義#########################

#########################宣告與設定#########################
frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)
delay = 0.002

#########################主程式#########################
while True:
    for duty_cycle in range(1023, -1, -1):
        led.duty(duty_cycle)
        sleep(delay)
    for duty_cycle in range(1024):
        led.duty(duty_cycle)
        sleep(delay)
