from machine import Pin, Timer
import time

led1=Pin(23, Pin.OUT, value=1)
led2=Pin(22, Pin.OUT, value=1)
led3=Pin(21, Pin.OUT, value=1)
x=1

def rgb():
  global x
  print(x)
  if x==1:
    led1.off()
    led2.on()
    led3.on()
  elif x==2:
    led1.on()
    led2.off()
    led3.on()
  else:
    led1.on()
    led2.on()
    led3.off()
  x+=1
  if x>3: x=1


OneShotTimer = Timer(0)
OneShotTimer.init(mode=Timer.PERIODIC, callback=lambda x: rgb(), freq=10)

while True:
  time.sleep(10)
  pass
