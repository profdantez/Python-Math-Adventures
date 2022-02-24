from turtle import *
import time

shape('turtle')
speed(0)

def square():
    '''Draw a square'''
    for i in range(4):
        forward(100)
        right(90)

def variable_square(sidelength=100):
    '''draw a square whose side length can be varied'''
    for i in range(4):
        forward(sidelength)
        right(90)

def triangle(sidelength=100):
    for i in range(3):
        right(120)
        forward(sidelength)

def right_triangle():
    right(90)
    forward(40)
    left(90)
    forward(30)
    left(135)
    forward(50)

length = 5
for i in range(60):
    variable_square(length)
    right(5)
    length += 5

time.sleep(10)