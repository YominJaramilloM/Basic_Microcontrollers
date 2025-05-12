from machine import Pin, PWM
import bluetooth
from BLE import BLEUART

def angle_servo(angle):
    maximum=128
    minimum=26 #CONVERSION A BITS DEL PUNTO MINIMO Y MAXIMO
    dutyC=int(minimum+(angle/180)*(maximum-minimum))
    pwm0.duty(dutyC)


p13=Pin(4, Pin.OUT)
p12=Pin(16, Pin.OUT)
p14=Pin(17, Pin.OUT)
pwm0 = PWM(Pin(14), duty=0) # create PWM object from a pin
pwm0.freq(50)         # get current frequency

p13.off()
p12.off()
p14.off()

nombre='YominJ' #nombre de la red bluetooth que se va a activar
ble=bluetooth.BLE()
uart= BLEUART(ble, nombre)
#Inicilización de modulo Bluetooth
def on_rx():
    rx_buffer=uart.read().decode().strip()
    uart.write("Respuesta ESP32:"+rx_buffer+'\n')
    if rx_buffer=="R":
        p13.off()
        p12.off()
        p14.on()
        angle_servo(0)
    if rx_buffer=="G":
        p13.on()
        p12.off()
        p14.off()
        angle_servo(90)
    if rx_buffer=="B":
        p13.off()
        p12.on()
        p14.off()
        angle_servo(170)
    if rx_buffer=="OFF":
        p13.off()
        p12.off()
        p14.off()
        angle_servo(0)
        

uart.irq(handler=on_rx)
        
        
