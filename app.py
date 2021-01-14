from flask import Flask, render_template, url_for, redirect
import RPi.GPIO as GPIO

app = Flask(__name__)


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



@app.route('/')
def main():
    return render_template("b3.html")

def change_dir(direction):
    if direction == 'left':
        pass

#        motor_left.ChangeDutyCycle(100)
#        motor_right.ChangeDutyCycle(0)
    elif direction == 'right':
        pass
#        motor_right.ChangeDutyCycle(100)
#        motor_left.ChangeDutyCycle(0)
    elif direction == 'forward':
        forward(50)
    elif direction == 'backward':
        backward(50)
    else:
        print("dont know that direction %s" % direction)
    time.sleep(3)
    init()
    

@app.route("/dir/left")
def route_left():
    change_dir('left')
    return redirect(url_for("main"))

@app.route("/dir/right")
def route_right():
    change_dir('right')
    return redirect(url_for("main"))

@app.route("/dir/forward")
def route_forward():
    change_dir('forward')
    return redirect(url_for("main"))   

@app.route("/dir/backward")
def route_backward():                           
    change_dir('backward')
    return redirect(url_for("main"))   

@app.route("/dir/stop")
def route_stop():
    stop_car()
    return redirect(url_for("main"))      
