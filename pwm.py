# Change these
pin = 12
frequencyHz = 1500

from RPi.GPIO import GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, frequencyHz)

dc = input("Duty cycle: ")
pwm.start(dc)

try:
    while True:
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.05)
        dc = input("Duty cycle: ")
except KeyboardInterrupt:
    print("Stopping")

pwm.stop()
GPIO.cleanup()
