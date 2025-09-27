from machine import Pin, ADC, PWM
from time import sleep
import UV
import network
import urequests
import gc

nc = Pin('LED',Pin.OUT)
oxsen = ADC(26)
oxdo = Pin(22,Pin.IN)
sensor = UV.LTR390()

url = 'http://192.168.8.3/data'

ssid = "Davey Jones"
password = "Pirate0723"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while wlan.status() !=3:
    sleep(0.2)
    nc.on()
    sleep(0.3)
    nc.off()
    if wlan.status() == 3:
        nc.off()
    
while True:
    aq = oxsen.read_u16()
    UVS = sensor.UVS()
    sleep(0.5)
    data = {
    "uv index": UVS,
    "aq index": aq
    }
    response = urequests.post(url, json=data)
    gc.collect()
    
    print(aq)
    print(oxdo.value())
    print("UVS: %d" %UVS)
    