#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Adafruit_PWM_Servo_Driver import PWM
import RPi.GPIO as GPIO
from ServoAgent import ServoAgent
import time
import sys
import serial

ser = serial.Serial("/dev/ttyAMA0", 9600)  # 串口波特率设置

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24

BtnPin = 19
Gpin = 5
Rpin = 6

TRIG = 20
ECHO = 21
# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=False)

# 手爪
clamp = ServoAgent(0, 10, 50, pwm, 28)

# 上臂电机
arm_a = ServoAgent(1, 10, 140, pwm, 90)

# 上臂电机
arm_b = ServoAgent(2, 40, 170, pwm, 90)

# 底座
bottom = ServoAgent(3, 0, 170, pwm, 90)
bottom.delta = 2

ServoDelayTime = 0.05  # 舵机响应时间

def t_up(speed, t_time):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, False)  # AIN2
    GPIO.output(AIN1, True)  # AIN1

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, False)  # BIN2
    GPIO.output(BIN1, True)  # BIN1
    time.sleep(t_time)


def t_stop(t_time):
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(AIN2, False)  # AIN2
    GPIO.output(AIN1, False)  # AIN1

    R_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN2, False)  # BIN2
    GPIO.output(BIN1, False)  # BIN1
    time.sleep(t_time)


def t_down(speed, t_time):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, True)  # AIN2
    GPIO.output(AIN1, False)  # AIN1

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, True)  # BIN2
    GPIO.output(BIN1, False)  # BIN1
    time.sleep(t_time)


def t_left(speed, t_time):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, True)  # AIN2
    GPIO.output(AIN1, False)  # AIN1

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, False)  # BIN2
    GPIO.output(BIN1, True)  # BIN1
    time.sleep(t_time)


def t_right(speed, t_time):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, False)  # AIN2
    GPIO.output(AIN1, True)  # AIN1

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, True)  # BIN2
    GPIO.output(BIN1, False)  # BIN1
    time.sleep(t_time)


def keysacn():
    val = GPIO.input(BtnPin)
    while GPIO.input(BtnPin) == False:
        val = GPIO.input(BtnPin)
    while GPIO.input(BtnPin) == True:
        time.sleep(0.01)
        val = GPIO.input(BtnPin)
        if val == True:
            GPIO.output(Rpin, 1)
            while GPIO.input(BtnPin) == False:
                GPIO.output(Rpin, 0)
        else:
            GPIO.output(Rpin, 0)


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(Gpin, GPIO.OUT)  # Set Green Led Pin mode to output
    GPIO.setup(Rpin, GPIO.OUT)  # Set Red Led Pin mode to output
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set BtnPin's mode is input, and pull up to high level(3.3V)

    GPIO.setup(AIN2, GPIO.OUT)
    GPIO.setup(AIN1, GPIO.OUT)
    GPIO.setup(PWMA, GPIO.OUT)

    GPIO.setup(BIN1, GPIO.OUT)
    GPIO.setup(BIN2, GPIO.OUT)
    GPIO.setup(PWMB, GPIO.OUT)
    pwm.setPWMFreq(50)  # Set frequency to 60 Hz


def Re_Servo():
    global clamp
    global arm_a
    global arm_b
    global bottom

    clamp.takePlace()
    arm_a.takePlace()
    arm_b.takePlace()
    bottom.takePlace()

    time.sleep(1)


def loop():
    while True:
        command = ser.read()
        ser.write(command + '\n')  # 回显
        if command == 'A':
            t_up(50, 0)  # 前进
        elif command == 'B':
            t_down(50, 0)  # 后退
        elif command == 'D':
            t_right(50, 0)  # 右转
        elif command == 'C':
            t_left(50, 0)  # 左转
        elif command == 'F':
            t_stop(0)  # 停止
        elif command == '0':
            ser.write("Servo all stop\n")
            # Servo_stop()
            time.sleep(ServoDelayTime)
        elif command == '1':  # 1
            ser.write("MeArm turn Left\n")
            bottom.increase()
            time.sleep(ServoDelayTime)
        elif command == '2':  # 2
            ser.write("MeArm turn Right\n")
            bottom.decrease()
            time.sleep(ServoDelayTime)
        elif command == '4':  # 4
            ser.write("Arm A Up\n")
            Arm_A_Up()
            time.sleep(ServoDelayTime)
        elif command == 'J':  # 上
            ser.write("Arm A Down\n")
            Arm_A_Down()
            time.sleep(ServoDelayTime)
        elif command == 'L':  # 左
            ser.write("Arm B Up\n")
            Arm_B_Up()
            time.sleep(ServoDelayTime)
        elif command == 'K':  # 下
            ser.write("Arm B Down\n")
            Arm_B_Down()
            time.sleep(ServoDelayTime)
        elif command == 'G':  # 打开手爪 （加速）
            ser.write("Clamp Open\n")
            ClampOpen()
        elif command == 'H':  # 闭合手爪 （减速）
            ser.write("Clamp Close\n")
            ClampClose()


def destroy():
    GPIO.cleanup()


def setupAll():
    global L_Motor
    global R_Motor

    setup()
    L_Motor = GPIO.PWM(PWMA, 100)
    L_Motor.start(0)
    R_Motor = GPIO.PWM(PWMB, 100)
    R_Motor.start(0)
    # keysacn()
    Re_Servo()


if __name__ == "__main__":
    setupAll()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
