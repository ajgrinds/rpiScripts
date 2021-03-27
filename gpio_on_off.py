import RPi.GPIO as GPIO
import time

# Change this if you want to use a different pin
pins = [11, 13, 37, 38]

GPIO.setmode(GPIO.BOARD)
for pin in pins:
  GPIO.setup(pin, GPIO.OUT)

while True:
  for pin in pins:
    GPIO.output(pin, 1)
  print("on")
  time.sleep(3)

  for pin in pins:
    GPIO.output(pin, 0)
  print("off")
  time.sleep(3)
  
