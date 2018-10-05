from gpiozero import *
from gpiozero.tools import *
from time import sleep
from signal import pause

sensor = LightSensor(21)
LED_1 = PWMLED(22)
for i in range(240):
    print (sensor.value)
    LED_1.value = sensor.value
    sleep(0.5)
print('finished')
LED_1.source = sensor.values
pause() 
