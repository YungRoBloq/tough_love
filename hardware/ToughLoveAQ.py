from machine import Pin, ADC, PWM
from time import sleep

oxsen = ADC(26)
oxdo = Pin(22,Pin.IN)


while True:
    aq = oxsen.read_u16()
    print(aq)
    print(oxdo.value())
    sleep(1)
    