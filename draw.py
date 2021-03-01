import turtle as t
import sys
import tty
import termios
import pygame


def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


t.setup(1200, 1000)
t.speed(10)
t.delay(0)
# t.tracer(False)
t.pensize(2)
t.pendown()


def go_ahead():
    t.forward(5)


def go_back():
    t.back(5)


def go_left():
    t.left(5)


def go_right():
    t.right(5)


def pen_up_down():
    if t.isdown():
        t.penup()
    else:
        t.pendown()



t.onkey(go_ahead, "Up")
t.onkey(go_back, "Down")
t.onkey(go_left, "Left")
t.onkey(go_right, "Right")
t.onkey(pen_up_down," ")
t.listen()
t.mainloop()
