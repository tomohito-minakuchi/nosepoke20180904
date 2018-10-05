from gpiozero import Button
from gpiozero import LED
from gpiozero import OutputDevice
from gpiozero.tools import sleep
import time
from datetime import datetime
import pandas as pd

## ============ CONSTANTS =============

IR_1 = Button(21)		# Infrared signal, green wire 
LED_1 = LED(22)
IR_2 = Button(19)
LED_2 = LED(20)
## 

## == poke record file initialization ==
start_time = time.time()
expdate = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
dfsuccess = pd.DataFrame([['start', start_time]] ,  columns=['id', 'time'])
dfright = pd.DataFrame([['start', start_time]] ,  columns=['id', 'time'])
dfwrong = pd.DataFrame([['start', start_time]] ,  columns=['id', 'time'])
dfsuccess.to_csv(expdate + "_pokesuccess.csv")
dfright.to_csv(expdate + "_rightpoke.csv")
dfwrong.to_csv(expdate + "_wrongpoke.csv")

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
    time.sleep(5)
    motor_1_pwm.off()
    time.sleep(5)
    motor_1_dir.off()
    motor_1_pwm.on()
    time.sleep(5)
    motor_1_pwm.off()
    poke_success = False
    
def reward_delivery():
    global poke_success
#    if IR_1.is_active and poke_success == False:        
    if poke_success == False:
       poke_time = time.time()
       poke_success = True
       temp = pd.DataFrame([['pokesuccess', poke_time - start_time]])
       temp.to_csv(expdate + "_pokesuccess.csv", mode='a', header = False)
       motor_down(motor_1_dir, motor_1_pwm)

def artreward_delivery():
    global poke_success
#    if IR_1.is_active and poke_success == False:        
    if poke_success == False:
       poke_time = time.time()
       poke_success = True
       motor_down(motor_1_dir, motor_1_pwm)


def rightpoke():
    poke_time = time.time()
    temp = pd.DataFrame([['poke', poke_time - start_time]])
    temp.to_csv(expdate + "_rightpoke.csv", mode='a', header = False) 
    print (poke_time, 'right poke')

def wrongpoke():
    poke_time = time.time()
    temp = pd.DataFrame([['poke', poke_time - start_time]])
    temp.to_csv(expdate + "_wrongpoke.csv", mode='a', header = False)
    print (poke_time, 'wrong poke')

LED_1.source = (IR_1.values)
LED_2.source = (IR_2.values)

motor_1_pwm.off()
motor_1_dir.off()

IR_1.when_released = rightpoke
IR_2.when_released = wrongpoke

while True:
    sleep(0.0001)
    if IR_1.is_pressed == False:
        print ('Reward delivery start!')
        reward_delivery()
    elif IR_2.is_pressed == False:
        print ('Artificial reward delivery start!')
        artreward_delivery()