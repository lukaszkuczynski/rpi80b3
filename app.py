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


def changeDuty(left_forward, right_forward, left_back, right_back):
    motor1_f.ChangeDutyCycle(left_forward)
    motor2_f.ChangeDutyCycle(right_forward)
    motor1_b.ChangeDutyCycle(left_back)
    motor2_b.ChangeDutyCycle(right_back)

def left(speed=30):
    print("turning left, with speed %d"%speed)
    changeDuty(0,speed,speed,0)

def right(speed=30):
    print("turning right, with speed %d"%speed)
    changeDuty(speed,0,0,speed)


def stop_car():
    print("car to stop!")
    changeDuty(0,0,0,0)

@app.route('/')
def main():
    return render_template("b3.html")

def change_dir(direction):
    if direction == 'left':
        left(25)
    elif direction == 'right':
        right(25)
    elif direction == 'forward':
        forward(40)
    elif direction == 'backward':
        backward(30)
    else:
        print("dont know that direction %s" % direction)
    #time.sleep(3)
    #init()
    

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
