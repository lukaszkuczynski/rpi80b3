import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)  

motor1_f = GPIO.PWM(12, 50)
motor1_b = GPIO.PWM(16, 50)

motor2_f = GPIO.PWM(13, 50)
motor2_b = GPIO.PWM(26, 50)

df = 0

def init():
    motor1_f.start(0)
    motor2_f.start(0)
    motor1_b.start(0)
    motor2_b.start(0)

init()

def forward(speed=50):
    print("Forward speed %d"%speed)
    motor1_f.ChangeDutyCycle(speed)
    motor2_f.ChangeDutyCycle(speed)
    motor1_b.ChangeDutyCycle(0)
    motor2_b.ChangeDutyCycle(0)
 

def backward(speed=50):
    print("Backward speed %d"%speed)
    motor1_f.ChangeDutyCycle(0)
    motor2_f.ChangeDutyCycle(0)
    motor1_b.ChangeDutyCycle(speed)
    motor2_b.ChangeDutyCycle(speed)

try:
    while True:
        forward(50)
        time.sleep(1)
        backward(50)
        time.sleep(1)
except KeyboardInterrupt:
    print('End of PWM-ing')
    led1.stop()
    GPIO.cleanup()
