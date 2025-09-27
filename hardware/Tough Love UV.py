import UV
from time import sleep
from machine import Pin

nc = Pin('LED',Pin.OUT)

if __name__ == '__main__':
    sensor = UV.LTR390()
    sleep(1)
    try:
        while True:
            nc.on()
            UVS = sensor.UVS()
            print("UVS: %d" %UVS)
            sleep(0.5)
            
    except KeyboardInterrupt:
        # sensor.Disable()
        exit()