# 	Turtle Graphics Game

import turtle 
import time 
import math
import random
import os


def screen_here():
	wn = turtle.Screen()
	wn.setup(width=0.7, height = 0.7)
	wn.bgcolor('lightgreen')
	wn.tracer(3)

screen_here()

while True:
	turtle.update()
	time.sleep(0.02)


