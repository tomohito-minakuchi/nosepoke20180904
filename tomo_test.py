from gpiozero import *
from gpiozero.tools import *
from time import sleep
from signal import pause

IR_1 = DigitalInputDevice(4, True)
LED_1 = LED(22)

LED_1.on()
sleep(1)
LED_1.off()
print(IR_1.value)
sleep(1)
LED_1.on()
for i in range(10):
    print(IR_1.value)
    LED_1.value = IR_1.value
    print(IR_1.value)
    sleep(0.5)

LED_1.source = IR_1.values
pause() 
