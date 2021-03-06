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
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.setposition(0,0)
		self.pendown()
		self.pen(fillcolor="black", pencolor="red", pensize=10)
		self.setheading(90)
		self.fd(160)

	def updating(self, c):
		self.clear()
		self.penup()
		self.setposition(0,0)
		self.pendown()
		self.setheading(c)
		self.fd(160)





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

arrow.resize(5,0.2)
print(arrow.heading())



#######################################################
# turtle.penup()
# turtle.setposition(0,0)
# turtle.pendown()
# turtle.pen(fillcolor="black", pencolor="red", pensize=10)

# turtle.setheading(90)
# turtle.fd(190)
arr_1 = Arrow()
c = 90 - 6
#######################################################







while True:
	turtle.update()
	time.sleep(1)

	i = arrow.heading()
	arrow.setheading(i-6)

#######################################################
	arr_1.updating(c)
	c = c -6
#######################################################









# Junk:

		# Shape 
# # (y,x) and when Y plus is a minus
# s = turtle.Shape("compound")
# poly1 = ((0,200),(0, 0))
# s.addcomponent(poly1, "lightgreen", "blue")
# turtle.register_shape("myshape", s)
# turtle.shape("myshape")

