from machine import Pin, I2C
import ssd1306

i2c = I2C(scl=Pin(1), sda=Pin(0))

WIDTH = 128
HEIGHT = 64

oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

def pain1():
    #index 1
    oled.fill(0)
    oled.text("                ", 0, 0)
    oled.text("   0        0   ", 0, 10)
    oled.text("  000      000  ", 0, 20)
    oled.text("                ", 0, 30)
    oled.text("   0000000000   ", 0, 40)
    oled.text("   0        0   ", 0, 50)
    oled.text("    00000000    ", 0, 60)
    oled.show()
    
def pain2():
#uv index 2
    oled.fill(0)
    oled.text("                ", 0, 0)
    oled.text("  000      000  ", 0, 10)
    oled.text("  0 0      0 0  ", 0, 20)
    oled.text("                ", 0, 30)
    oled.text("  00        00  ", 0, 40)
    oled.text("   0000  0000   ", 0, 50)
    oled.text("      0000     ", 0, 60)
    oled.show()

def pain3():
#uv index 3
    oled.fill(0)
    oled.text("                ", 0, 0)
    oled.text("  0 0      0 0  ", 0, 10)
    oled.text("  000      000  ", 0, 20)
    oled.text("                ", 0, 30)
    oled.text("  0          0  ", 0, 40)
    oled.text("   0000  0000   ", 0, 50)
    oled.text("       00       ", 0, 60)
    oled.show()


def pain4():
#uv index 4
    oled.fill(0)
    oled.text("                ", 0, 0)
    oled.text("  000      000  ", 0, 10)
    oled.text("  000      000  ", 0, 20)
    oled.text("                ", 0, 30)
    oled.text("  0          0  ", 0, 40)
    oled.text("   0000000000   ", 0, 50)
    oled.text("               ", 0, 60)
    oled.show()

def pain5():
    
#uv index 5
    oled.fill(0)
    oled.text("                ", 0, 0)
    oled.text("                ", 0, 10)
    oled.text("  000      000  ", 0, 20)
    oled.text("                ", 0, 30)
    oled.text("                ", 0, 40)
    oled.text("    00000000    ", 0, 50)
    oled.text("                ", 0, 60)
    oled.show()


def pain6():
#uv index 6
    oled.fill(0)
    oled.text("                ", 0, 0)
    oled.text("   0        0   ", 0, 10)
    oled.text("  000      000  ", 0, 20)
    oled.text("                ", 0, 30)
    oled.text("                ", 0, 40)
    oled.text("      0000      ", 0, 50)
    oled.text("                ", 0, 60)
    oled.show()


def pain7():
#uv index 7
    oled.fill(0)
    oled.text("                ", 0, 0)
    oled.text("  000      000  ", 0, 10)
    oled.text("   0        0   ", 0, 20)
    oled.text("                ", 0, 30)
    oled.text("      0000      ", 0, 40)
    oled.text("      0  0       ", 0, 50)
    oled.text("                ", 0, 60)
    oled.show()
    
def pain8():
#uv index 8
    oled.fill(0)
    oled.text("  000      000  ", 0, 0)
    oled.text("  0 0      0 0  ", 0, 10)
    oled.text("  000      000  ", 0, 20)
    oled.text("                ", 0, 30)
    oled.text("     000000      ", 0, 40)
    oled.text("     0    0     ", 0, 50)
    oled.text("     000000     ", 0, 60)
    oled.show()

def pain9():
#uv index 9
    oled.fill(0)
    oled.text("                ", 0, 0)
    oled.text("  000      000  ", 0, 10)
    oled.text("  000      000  ", 0, 20)
    oled.text("                ", 0, 30)
    oled.text("     000000     ", 0, 40)
    oled.text("    00    00    ", 0, 50)
    oled.text("                ", 0, 60)
    oled.show()
    
def pain10():
#uv index 10
    oled.fill(0)
    oled.text("  0 0      0 0  ", 0, 0)
    oled.text("   0        0   ", 0, 10)
    oled.text("  0 0      0 0  ", 0, 20)
    oled.text("                ", 0, 30)
    oled.text("    00000000    ", 0, 40)
    oled.text("   00      00   ", 0, 50)
    oled.text("                ", 0, 60)
    oled.show()

def pain11():
#uv index 11
    oled.fill(0)
    oled.text("   000000000    ", 0, 5)
    oled.text("    0000000     ", 0, 10)
    oled.text("     00000      ", 0, 15)
    oled.text("     00000      ", 0, 20)
    oled.text("      000       ", 0, 25)
    oled.text("      000       ", 0, 30)
    oled.text("       0        ", 0, 35)
    oled.text("       0        ", 0, 40)
    oled.text("                ", 0, 50)
    oled.text("      000       ", 0, 55)
    oled.text("      000       ", 0, 60)
    oled.show()