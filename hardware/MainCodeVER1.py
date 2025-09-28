from machine import Pin, ADC, PWM, I2C
from time import sleep
import ssd1306
import UV
import network
import urequests
import gc
import random
import Faces


nc = Pin('LED',Pin.OUT)
oxsen = ADC(26)
oxdo = Pin(22,Pin.IN)
sensor = UV.LTR390()

Test = Pin(6,Pin.IN)

i2c = I2C(1,scl=Pin(3), sda=Pin(2))
WIDTH = 128
HEIGHT = 64
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

url = 'http://192.168.8.3:8000/data'

ssid = "Davey Jones"
password = "Pirate0723"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while wlan.status() !=3:
    oled.fill(0)
    oled.text("Connecting",0,10)
    oled.show()
    sleep(0.2)
    nc.on()
    sleep(0.3)
    nc.off()
    if wlan.status() == 3:
        oled.fill(0)
        oled.text("Connected",0,10)
        oled.show()
        nc.off()
        
while True:
    
    while Test.value() == 1 :
        aq = oxsen.read_u16()
        UVS = sensor.UVS()
        sleep(0.5)
        if UVS == 0:
            oled.fill(0)
            oled.text("Raw Values", 15, 0)
            oled.text("Air Quality:",0,10)
            oled.text(str(aq),0,20)
            oled.text("UV index:",0,30)
            oled.text(str(UVS),0,40)
            oled.show()
        elif UVS == 1:
            Faces.pain1()
        elif UVS == 2:
            Faces.pain2()
        elif UVS == 3:
            Faces.pain3()
        elif UVS == 4:
            Faces.pain4()
        elif UVS == 5:
            Faces.pain5()
        elif UVS == 6:
            Faces.pain6()
        elif UVS == 7:
            Faces.pain7()
        elif UVS == 8:
            Faces.pain8()
        elif UVS == 9:
            Faces.pain9()
        elif UVS == 10:
            Faces.pain10()
        elif UVS == 11:
            Faces.pain11()
        
        ox = {
        "type": "aq",
        "sensor_id": 1,
        "value": aq
        }
        uv = {
        "type": "uv",
        "sensor_id": 1,
        "value" : UVS
        }
        
        response = urequests.post(url, json=ox )
        response = urequests.post(url, json=uv )
        gc.collect()
        
    sleep(2)
    while Test.value() == 0 :
        aq = random.randint(0, 60000)
        UVS = random.randint(1, 11)
        sleep(0.5)
        if UVS == 0:
            oled.fill(0)
            oled.text("Raw Values", 15, 0)
            oled.text("Air Quality:",0,10)
            oled.text(str(aq),0,20)
            oled.text("UV index:",0,30)
            oled.text(str(UVS),0,40)
            oled.show()
        elif UVS == 1:
            Faces.pain1()
        elif UVS == 2:
            Faces.pain2()
        elif UVS == 3:
            Faces.pain3()
        elif UVS == 4:
            Faces.pain4()
        elif UVS == 5:
            Faces.pain5()
        elif UVS == 6:
            Faces.pain6()
        elif UVS == 7:
            Faces.pain7()
        elif UVS == 8:
            Faces.pain8()
        elif UVS == 9:
            Faces.pain9()
        elif UVS == 10:
            Faces.pain10()
        elif UVS == 11:
            Faces.pain11()
        
        ox = {
        "type": "aq",
        "sensor_id": 1,
        "value": aq
        }
        uv = {
        "type": "uv",
        "sensor_id": 1,
        "value" : UVS
        }
        
        response = urequests.post(url, json=ox )
        response = urequests.post(url, json=uv )
        gc.collect()
        
        
        
        
        
