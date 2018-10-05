from gpiozero import *
from gpiozero.tools import *
import time

## ============ CONSTANTS =============

IR_ACTIVATION_TIME = .01				# Poke-time to activate platform
PLT_DOWN_TIME = 5					# Stay-time for platform after activation

## ============ VARIABLES =============
## Initiation Values 

poke_success = True					# Determinator of platform activation



## ============ OUTPUTS =============== 


#IR_1 = Button(12)
#LED_1 = LED(19)
poker_LED = LED(19)


IR_1 = Button(12, pull_up = False, hold_time = IR_ACTIVATION_TIME)		# Infrared signal, green wire 


motor_1_dir = OutputDevice(4, active_high = False, initial_value = False)
motor_1_pwm = OutputDevice(17, active_high = True, initial_value = True)

## ============ Functions =====================    

def motor_down(motor_1_dir, motor_1_pwm):
    global poke_success
    motor_1_dir.on()
    motor_1_pwm.on()
    sleep(4.5)
    motor_1_pwm.off()
    sleep(5)
    motor_1_dir.off()
    motor_1_pwm.on()
    sleep(5)
    motor_1_pwm.off()
    poke_success = False
    poker_LED.on()


def IR_held():
    global poke_success
    poker_LED.off()
    if IR_1.is_active and poke_success == False:
        poke_success = True
        motor_down(motor_1_dir, motor_1_pwm)
    else:
        print "poker blocked"


## ============ Program Start =================
LED_1.source = (IR_1.values)

sleep(5)

motor_1_pwm.off()
motor_1_dir.off()
poker_LED.on()


IR_1.when_held = IR_held
