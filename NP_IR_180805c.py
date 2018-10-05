from gpiozero import *
from gpiozero.tools import *
import time

## ============ CONSTANTS =============
IR_ACTIVATION_TIME = .01				# Poke-time to activate platform
PLT_DOWN_TIME = 5					# Stay-time for platform after activation
RETRACTION_TIME = 4					# Time for platform to go back up
LOCKOUT_TIME = 0						# Time for poker to stay inactive after retraction
TOTAL_RETRACTION_TIME = RETRACTION_TIME + LOCKOUT_TIME 


## ============ VARIABLES =============
## Initiation Values 
PLT_SW_1 = 0
PLT_SW_2 = 0 # Initiation time of platform swtich 
PLT_retract_init = 0
poked_side = 0
poke_success = False					# Determinator of platform activation


## ============ OUTPUTS =============== 
#IR_1_TDT = DigitalOutputDevice(18)		# Cue to TDT
IR_1 = Button(12, pull_up = False, hold_time = IR_ACTIVATION_TIME)		# Infrared signal, green wire 
#PLT_SW_1_DOWN = Button(12, pull_up=False, hold_time = PLT_DOWN_TIME)	# Platform switch
#PLT_SW_1_TDT = DigitalOutputDevice(6)

#IR_2_TDT = DigitalOutputDevice(13)		# Cue to TDT
#IR_2 = Button(24, pull_up = False, hold_time = IR_ACTIVATION_TIME, hold_repeat=True)		# Infrared signal 
#PLT_SW_2_DOWN = Button(16,  pull_up=False, hold_time = PLT_DOWN_TIME)	# Platform switch
#PLT_SW_2_TDT = DigitalOutputDevice(5)

poker_LED = LED(19)
#LED_TDT = DigitalOutputDevice (26)#blue wire			# LED indicating poker activation

motor_1_dir = OutputDevice(4, active_high = False, initial_value = False)
motor_1_pwm = OutputDevice(17, active_high = True, initial_value = True)
#motor_2_dir = OutputDevice(27, active_high = False, initial_value = False)
#motor_2_pwm = OutputDevice(22, active_high = True, initial_value = True)


## ============ Functions =====================    
def motor_down(motor_dir, motor_pwm):
    global poke_success
    motor_dir.on()
    motor_pwm.on()
    sleep(4.5)
    motor_pwm.off()
    sleep(5)
    motor_dir.off()
    motor_pwm.on()
    sleep(5)
    motor_pwm.off()
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

#IR_1_TDT.source=(IR_1.values)
#IR_2_TDT.source=(IR_2.values)
#LED_TDT.source = poker_LED.values

sleep(1)

motor_1_pwm.off()
#motor_2_pwm.off()
motor_1_dir.off()
#motor_2_dir.off()
poker_LED.on()


IR_1.when_held = IR_held
IR_2.when_held = IR_held
