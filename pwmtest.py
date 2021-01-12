import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
 
led1 = GPIO.PWM(12, 50)
led2 = GPIO.PWM(16, 50)
df = 0
led1.start(df)
led2.start(df)
 
try:
    while True:
        for dc in range(0,101,5):
            led1.ChangeDutyCycle(dc)
            led2.ChangeDutyCycle(100-dc)
            time.sleep(0.1)
        for dc in range(100,0,-5):
            led1.ChangeDutyCycle(dc)
            led2.ChangeDutyCycle(100-dc)
            time.sleep(0.02)
except KeyboardInterrupt:
    print('End of PWM-ing')
    led1.stop()
    GPIO.cleanup()
