from gpiozero import *
from gpiozero.tools import *
from time import sleep

IR_1 = Button(21)
LED_1 = LED(22)
for i in range(60):
    print (IR_1.value)
    LED_1.value = IR_1.value
    sleep(0.5)
print('finished')
LED_1.source = IR_1.values

# Direction set to not active high == goes up when False
##motor_dir = OutputDevice(4, active_high = True, initial_value = False)
### PWM turns on when True
##motor_pwm = OutputDevice(17, active_high = True, initial_value = True)
##
                                                            
