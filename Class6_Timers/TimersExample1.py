from machine import Pin, Timer
import time

def Encender(x):
    led3.on()

def Apagar(x):
    led3.off()


p1= Pin(25, Pin.IN, Pin.PULL_DOWN)
led1=Pin(19, Pin.OUT)
led2=Pin(18, Pin.OUT)
led3=Pin(5,Pin.OUT)

Azul= Timer(0)
Azul.init(mode=Timer.PERIODIC, callback=Encender, period=1000)


Azul2= Timer(1)
Azul2.init(mode=Timer.PERIODIC, callback=Apagar, period=2000)


while True:
    if(p1.value()==1):
        while(p1.value()==1):
            pass

        print(p1.value())
            
    