# Change these
pin = 33
frequencyHz = 1000

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, frequencyHz)

dc = int(input("Duty cycle: "))
pwm.start(dc)

try:
    while True:
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.05)
        dc = int(input("Duty cycle: "))
except KeyboardInterrupt:
    print("Stopping")

pwm.stop()
GPIO.cleanup()
