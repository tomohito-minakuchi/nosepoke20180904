from gpiozero import *
from gpiozero.tools import *


## ============ CONSTANTS =============

IR_1 = Button(21)		# Infrared signal, green wire 
LED_1 = LED(22)
## 

poke_success = False					# Determinator of platform activation


# Direction set to not active high == goes up when False
motor_1_dir = OutputDevice(4, active_high = False, initial_value = False)
### PWM turns on when True
motor_1_pwm = OutputDevice(17, active_high = True, initial_value = True)
##

def motor_down(motor_1_dir, motor_1_pwm):
    global poke_success
    motor_1_dir.on()
    motor_1_pwm.on()
    sleep(5)
    motor_1_pwm.off()
    sleep(5)
    motor_1_dir.off()
    motor_1_pwm.on()
    sleep(5)
    motor_1_pwm.off()
    poke_success = False
    
def IR_held():
    global poke_success
    if IR_1.is_active and poke_success == False:
        poke_success = True
        motor_down(motor_1_dir, motor_1_pwm)

LED_1.source = (IR_1.values)

motor_1_pwm.off()
motor_1_dir.off()

IR_1.when_held = IR_held
# print(poke_success)
