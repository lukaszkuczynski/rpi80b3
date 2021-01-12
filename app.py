from flask import Flask, render_template, url_for, redirect
import RPi.GPIO as GPIO

app = Flask(__name__)


import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
 
motor_left = GPIO.PWM(12, 50)
motor_right = GPIO.PWM(16, 50)
df = 0
motor_left.start(df)
motor_right.start(df)
 


@app.route('/')
def main():
    return render_template("b3.html")

def change_dir(direction):
    if direction == 'left':
        motor_left.ChangeDutyCycle(100)
        motor_right.ChangeDutyCycle(0)
    elif direction == 'right':
        motor_right.ChangeDutyCycle(100)
        motor_left.ChangeDutyCycle(0)
    else:
        print("dont know that direction %s" % direction)
    

@app.route("/dir/left")
def left():
    change_dir('left')
    return redirect(url_for("main"))

@app.route("/dir/right")
def right():
    change_dir('right')
    return redirect(url_for("main"))
