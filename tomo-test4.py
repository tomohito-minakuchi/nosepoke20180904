from gpiozero import *
from gpiozero.tools import *
from time import sleep
from signal import pause

sensor = LightSensor(21)
LED_1 = PWMLED(22)

for i in range(60000):
    print (sensor.value)
    if sensor.value < 0.9:
        LED_1.value = 0
    else:
        LED_1.value = 0.5
#    LED_1.value = sensor.value
    sleep(0.01)
print('finished')

# LED_1.source = sensor.values
# pause() 
