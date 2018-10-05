import RPi.GPIO as GPIO
from time import sleep

num = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(num, GPIO.OUT)

for i in range (2):
    GPIO.output(num, GPIO.HIGH)
    sleep(1)
    GPIO.output(num, GPIO.LOW)
    sleep(1)
    print (GPIO)
