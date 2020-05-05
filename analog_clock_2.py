# 	Turtle Graphics Game

import turtle 
import time 
import math
import random
import os

SQUARE 		= 4
TRIANGLE 	= 3
PENTAGON	= 5
HEXAGON		= 6
global c


def screen_here():
	wn = turtle.Screen()
	wn.setup(width=0.7, height = 0.7)
	wn.bgcolor('lightgreen')
	wn.tracer(3)


def draw_shape(shape):

	if shape == 'square':
		turtle.color('red')
		for i in range(0,4):
			turtle.fd(400)
			turtle.lt(90)
		# turtle.fd(75)



screen_here()

# Square
turtle.color('lightgreen')
turtle.goto(-200, -200)
draw_shape('square')


# Circle
turtle.color('lightgreen')
turtle.setposition(0,-195)
turtle.color('darkred')
turtle.circle(195)

# Clock Face
class Quaters(turtle.Turtle):
	def __init__(self, shape, color, startx, starty):
		turtle.Turtle.__init__(self)
		self.shape(shape)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)

	def resize(self, wid_a, len_b):
		self.shapesize(stretch_wid = wid_a, stretch_len = len_b , outline = None)



class Arrow(turtle.Turtle):
	def __init__(self, arr_len, pen_size):
		turtle.Turtle.__init__(self)
		self.penup()
		self.setposition(0,0)
		self.pendown()
		self.pen(fillcolor="black", pencolor="red", pensize=pen_size)
		self.setheading(90)
		self.fd(arr_len)

	def updating(self, c, arr_len):
		self.clear()
		self.penup()
		self.setposition(0,0)
		self.pendown()
		self.setheading(c)
		self.fd(arr_len)





corr_quarter = [[-180,0], [0,180], [180,0], [0,-180]]

sq_1  = Quaters('square', 'black', -180, 0)
sq_2  = Quaters('square', 'black', 0, 180)
sq_3  = Quaters('square', 'black', 180, 0)
sq_4  = Quaters('square', 'black', 0, -180)

sq_5  = Quaters('square', 'black', 155.8, 90)
sq_6  = Quaters('square', 'black', 90, 155.8)

sq_7  = Quaters('square', 'black', -90, 155.8)
sq_8  = Quaters('square', 'black', -155.8, 90)

sq_9  = Quaters('square', 'black', -155.8, -90)
sq_10  = Quaters('square', 'black', -90, -155.8)

sq_11  = Quaters('square', 'black', 90, -155.8)
sq_12  = Quaters('square', 'black', 155.8, -90)

arrow  = Quaters('square', 'black', 0, 80)




#######################################################
arr_sec = Arrow(150,3)
arr_min = Arrow(170,6)
arr_hrs = Arrow(100,12)
#######################################################







while True:
	turtle.update()
	time.sleep(1)

#######################################################
	b = time.ctime().split()
	d = b[3].split(':')
	sec   = 90 - 6* int(d[2])
	mins  = 90 - 6* int(d[1])
	hours = 90 - 6* int(d[0])

	arr_sec.updating(sec, 150)
	arr_min.updating(mins, 170)
	arr_hrs.updating(hours, 100)
#######################################################



