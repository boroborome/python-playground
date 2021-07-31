#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Servo import *

setupAll()
t_up(50, 3)
t_right(50, 0.55)
t_up(50, 6)
t_stop(2)

ClampOpen()
Arm_A(120)
Arm_B(150)
Bottom(85)
ClampClose()

Arm_B(90)

ClampOpen()
Arm_B(50)
Arm_A(120)
Bottom(85)
time.sleep(0.5)
Arm_B(155)
time.sleep(0.5)
ClampClose()
time.sleep(0.5)
Arm_B(50)
time.sleep(0.5)
Bottom(5)
time.sleep(0.5)
Arm_B(150)
time.sleep(0.5)
ClampOpen()

