from gpiozero import *
from gpiozero.tools import *

## ============ CONSTANTS =============

IR_ACTIVATION_TIME = 0.1				# Poke-time to activate platform
PLT_DOWN_TIME = 5					# Stay-time for platform after activation


## ============ VARIABLES =============
## Initiation Values 

poke_success = False					# Determinator of platform activation


## ============ OUTPUTS =============== 

##IR_1 = Button(12)
LED_1 = LED(19)
##

IR_1 = Button(12, pull_up = False, hold_time = IR_ACTIVATION_TIME)		# Infrared signal, green wire 


# Direction set to not active high == goes up when False
motor_dir = OutputDevice(4, active_high = True, initial_value = False)
### PWM turns on when True
motor_pwm = OutputDevice(17, active_high = True, initial_value = True)
##


LED_1.source = (IR_1.values)
